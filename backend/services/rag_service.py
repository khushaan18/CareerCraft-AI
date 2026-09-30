"""Retrieval-Augmented Generation service for CareerCraft AI.

Knowledge sources are curated career/ATS guidance documents under data/knowledge.
The service uses Sentence-Transformers embeddings and ChromaDB for retrieval.
No agents or LangGraph are used.
"""
from functools import lru_cache
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE_DIR = ROOT / "data" / "knowledge"
DB = ROOT / "chroma_db"
COLLECTION = "careercraft_knowledge"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def _embeddings():
    from langchain_community.embeddings import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def build_index(force: bool = False) -> int:
    """Build or rebuild the persistent Chroma index from the knowledge base."""
    from langchain_community.document_loaders import TextLoader
    from langchain_community.vectorstores import Chroma
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    files = sorted(KNOWLEDGE_DIR.glob("*.txt"))
    if not files:
        raise FileNotFoundError(f"No knowledge files found in {KNOWLEDGE_DIR}")

    if force and DB.exists():
        import shutil
        shutil.rmtree(DB)
        retriever.cache_clear()

    docs = []
    for path in files:
        docs.extend(TextLoader(str(path), encoding="utf-8").load())

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=700, chunk_overlap=120
    ).split_documents(docs)
    for chunk in chunks:
        chunk.metadata["source"] = Path(chunk.metadata.get("source", "unknown")).name

    DB.mkdir(parents=True, exist_ok=True)
    Chroma.from_documents(
        documents=chunks,
        embedding=_embeddings(),
        persist_directory=str(DB),
        collection_name=COLLECTION,
    )
    retriever.cache_clear()
    return len(chunks)


@lru_cache(maxsize=1)
def retriever():
    """Return the persistent Chroma retriever, building it automatically if needed."""
    from langchain_community.vectorstores import Chroma

    if not DB.exists() or not any(DB.iterdir()):
        build_index()

    store = Chroma(
        persist_directory=str(DB),
        embedding_function=_embeddings(),
        collection_name=COLLECTION,
    )
    return store.as_retriever(search_kwargs={"k": 4})


def retrieve(query: str) -> List[str]:
    """Retrieve grounded guidance text for a query."""
    try:
        return [doc.page_content for doc in retriever().invoke(query)]
    except Exception:
        return []


def retrieve_with_sources(query: str) -> List[Dict[str, str]]:
    """Retrieve guidance together with its knowledge-base source filename."""
    try:
        docs = retriever().invoke(query)
        return [
            {"content": d.page_content, "source": d.metadata.get("source", "unknown")}
            for d in docs
        ]
    except Exception:
        return []


def status() -> Dict[str, object]:
    """Return a simple, user-facing RAG health/status payload."""
    knowledge_files = sorted(KNOWLEDGE_DIR.glob("*.txt"))
    indexed = DB.exists() and any(DB.iterdir())
    return {
        "enabled": True,
        "vector_store": "ChromaDB",
        "embedding_model": EMBEDDING_MODEL,
        "knowledge_files": [p.name for p in knowledge_files],
        "index_present": indexed,
        "knowledge_directory": str(KNOWLEDGE_DIR),
    }
