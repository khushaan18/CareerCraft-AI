"""Explicit knowledge-base ingestion entry point for CareerCraft AI RAG."""
from backend.services.rag_service import build_index

if __name__ == "__main__":
    chunks = build_index(force=True)
    print(f"CareerCraft RAG knowledge base indexed: {chunks} chunks")
