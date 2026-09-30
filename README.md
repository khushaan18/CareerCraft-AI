# CareerCraft AI — Generative AI + RAG Resume & Career Assistant

CareerCraft AI is a **non-agentic Generative AI application** that analyzes resumes against job descriptions and produces explainable, grounded career-document recommendations.

It combines **Groq + LangChain + FastAPI + Streamlit + Sentence-Transformers + ChromaDB RAG**. There is **no LangGraph and no autonomous/multi-agent layer**.

## What makes this a real RAG project?

CareerCraft has a persistent knowledge base under `data/knowledge/` containing curated resume-writing and ATS guidance. The RAG pipeline:

```text
Knowledge documents
      ↓
Recursive chunking
      ↓
Sentence-Transformers embeddings
      ↓
ChromaDB persistent vector store
      ↓
Query built from the target job + detected skill gaps
      ↓
Top-k relevant guidance chunks
      ↓
Groq LLM prompt context
      ↓
Grounded resume / ATS / cover-letter generation
```

The retrieved material is **guidance**, not candidate evidence. Candidate facts always come from the uploaded resume and job description.

## RAG components

- **Vector database:** ChromaDB
- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Chunking:** LangChain `RecursiveCharacterTextSplitter`
- **Knowledge source:** `data/knowledge/*.txt`
- **Retriever:** Chroma similarity search, top 4 chunks
- **Generation:** Groq through LangChain
- **Observability:** LangSmith configuration is available

RAG is automatically initialized when the application first needs it. You can also explicitly rebuild it:

```bash
python -m scripts.ingest_knowledge
```

or use the **Rebuild Knowledge Index** button in the Streamlit sidebar.

## Kaggle evaluation datasets

The project includes reproducible download support for:

1. **Resume Dataset — Snehaan Bhawal**  
   https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

2. **Resume Skill Gap Analyzer Dataset — Keerthika**  
   https://www.kaggle.com/datasets/keerthiramesh470/resume-skill-gap-analyzer-dataset

The full third-party datasets are not redistributed in this ZIP. Download them using your Kaggle account and follow the current dataset licenses/terms.

```bash
python scripts/download_kaggle_data.py
```

They are for **evaluation/benchmarking**, not for training Groq.

## Evaluation dashboard

A repeatable benchmark is included under `data/evaluation/`.

Run:

```bash
python scripts/run_evaluation.py
```

or view the **Evaluation** tab in Streamlit.

Current benchmark metrics include:

- label accuracy
- mean required-skill coverage
- benchmark example count
- Kaggle dataset download status

## Application features

- PDF/DOCX/TXT resume parsing
- Structured resume extraction
- Job-description extraction
- Semantic + keyword job alignment
- Skill-gap analysis
- ATS-oriented heuristic analysis
- RAG-grounded resume optimization
- RAG-grounded cover-letter generation
- Interview-question generation
- Unsupported-claim / hallucination checks
- RAG evidence/source display
- DOCX/PDF exports
- SQLite history
- Evaluation dashboard
- Docker support
- Unit tests

## Architecture

```text
Streamlit UI
     ↓ REST
FastAPI
     ↓
GenAI Service
 ├── Resume Parser
 ├── Job Analyzer
 ├── Semantic Matcher
 ├── RAG Retriever ──→ Sentence-Transformers ──→ ChromaDB
 └── Groq Structured Generation
          ↓
 Resume / ATS / Skill Gap / Cover Letter / Interview Outputs
          ↓
 Quality Checker + Evaluation
```

**No LangGraph. No agents. No autonomous orchestration.**

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` from `.env.example` and set:

```env
GROQ_API_KEY=your_key_here
GROQ_MODEL=llama-3.3-70b-versatile
LANGSMITH_API_KEY=
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=careercraft-ai
BACKEND_URL=http://localhost:8000
```

Start the backend:

```bash
uvicorn backend.main:app --reload --port 8000
```

Start the frontend in another terminal:

```bash
streamlit run app/streamlit_app.py
```

Open `http://localhost:8501`.

## Testing

```bash
pytest -q
```

## Project structure

```text
CareerCraft-AI/
├── app/
│   └── streamlit_app.py
├── backend/
│   ├── main.py
│   ├── llm.py
│   ├── prompts.py
│   ├── schemas/
│   ├── parsers/
│   └── services/
│       ├── genai_service.py
│       ├── rag_service.py
│       ├── matching_service.py
│       ├── history.py
│       └── exporter.py
├── data/
│   ├── knowledge/
│   ├── evaluation/
│   └── raw/kaggle/
├── evaluation/
├── scripts/
│   ├── ingest_knowledge.py
│   ├── download_kaggle_data.py
│   └── run_evaluation.py
├── tests/
├── .env.example
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## Important limitation

The ATS score is an application heuristic, not a proprietary ATS score, and the system does not guarantee interviews or employment. The LLM must not invent candidate facts.
