# ✦ CareerCraft AI

### AI-Powered Resume & Career Assistant

**Turn a resume and a job description into a personalized application
strategy.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-LLM%20Framework-1C3C3C?style=for-the-badge)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-FF6B6B?style=for-the-badge)](https://www.trychroma.com/)
[![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-F55036?style=for-the-badge)](https://groq.com/)

------------------------------------------------------------------------

## 🚀 What is CareerCraft AI?

Applying for a job is more than matching keywords.

A resume can contain strong technical experience but still fail to
communicate the right skills for a particular role. CareerCraft AI was
built to make this process more structured.

The application takes:

**Resume + Job Description**

and produces:

-   📊 Job alignment analysis
-   🎯 ATS-oriented analysis
-   🧩 Skill-gap identification
-   ✍️ Tailored resume recommendations
-   💌 Cover-letter generation
-   🎤 Interview-question generation
-   📚 RAG-grounded career guidance
-   📄 Resume, cover-letter and report exports
-   🧪 Evaluation metrics for the system

------------------------------------------------------------------------

## ✨ Core Features

  📄 Resume Parsing                   Extracts structured information
                                      from PDF, DOCX and TXT resumes

  💼 Job Analysis                     Identifies role, skills, keywords
                                      and requirements from a job
                                      description

  🔎 Semantic Matching                Compares resume capabilities with
                                      job requirements

  🎯 ATS Analysis                     Examines keyword coverage and
                                      resume structure

  🧩 Skill Gap Analysis               Separates matched, partial and
                                      missing skills

  🧠 RAG                              Retrieves relevant resume/ATS
                                      guidance from a knowledge base

  ✍️ Resume Optimization              Generates role-specific
                                      improvements grounded in the
                                      supplied resume

  💌 Cover Letter                     Creates a personalized cover letter

  🎤 Interview Prep                   Generates interview questions based
                                      on the resume and target role

  🛡️ Quality Check                    Reviews generated outputs for
                                      quality and consistency

  📥 Export                           Generates DOCX and PDF outputs

  🗃️ History                          Stores previous analyses locally

  📈 Evaluation                       Provides benchmark/evaluation
                                      functionality


## 🧠 System Architecture

``` mermaid
flowchart TD
    A[Resume PDF / DOCX / TXT] --> B[Document Parser]
    J[Job Description] --> C[Job Analysis]

    B --> D[Structured Resume Profile]
    C --> E[Structured Job Profile]

    D --> F[Semantic + Keyword Matching]
    E --> F

    F --> G[Skill Gap Analysis]

    E --> H[RAG Query Builder]
    G --> H
    H --> I[Sentence Transformer]
    I --> K[ChromaDB Knowledge Base]
    K --> L[Relevant Career Guidance]

    D --> M[Groq LLM]
    E --> M
    L --> M

    M --> N[Optimized Resume]
    M --> O[Cover Letter]
    M --> P[Interview Questions]
    M --> Q[ATS Analysis]
    M --> R[Quality Check]

    N --> S[Streamlit UI]
    O --> S
    P --> S
    Q --> S
    R --> S
    F --> S
    G --> S
```

------------------------------------------------------------------------

## 🏗️ Project Architecture

``` text
CareerCraft-AI/
│
├── app/
│   └── streamlit_app.py
│
├── backend/
│   ├── config.py
│   ├── llm.py
│   ├── main.py
│   ├── prompts.py
│   │
│   ├── parsers/
│   │   └── document_parser.py
│   │
│   ├── schemas/
│   │   └── models.py
│   │
│   ├── services/
│   │   ├── genai_service.py
│   │   ├── history.py
│   │   ├── matching_service.py
│   │   ├── rag_service.py
│   │   └── exporter.py
│   │
│   └── utils/
│       └── text.py
│
├── data/
│   ├── knowledge/
│   │   ├── ats_guidelines.txt
│   │   ├── bullet_writing.txt
│   │   └── resume_guidelines.txt
│   │
│   ├── raw/
│   │   └── kaggle/
│   │
│   └── evaluation/
│
├── evaluation/
│   ├── evaluator.py
│   └── metrics.py
│
├── scripts/
│   ├── ingest_knowledge.py
│   ├── download_kaggle_data.py
│   └── run_evaluation.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

------------------------------------------------------------------------

## 🔥 How the Application Works

### 1. Upload Resume

The user uploads a resume in PDF, DOCX or TXT format.

### 2. Extract Resume Information

The document parser converts the uploaded file into text.

The Generative AI layer then extracts structured resume information
using Pydantic schemas.

### 3. Analyze the Job Description

The target job description is processed into a structured job profile
containing information such as:

-   Target role
-   Required skills
-   Keywords
-   Experience requirements
-   Relevant technologies

### 4. Compare Resume and Job

The matching layer performs deterministic semantic/keyword comparison.

It identifies:

``` text
Matched Skills
      ↓
Partial Matches
      ↓
Missing Skills
      ↓
Learning Priorities
```

### 5. Retrieve Relevant Guidance

The system creates a context-aware query using information such as the
target role, required skills and missing skills.

Sentence Transformer embeddings are used to retrieve relevant documents
from ChromaDB.

------------------------------------------------------------------------

## 🧩 RAG Implementation

CareerCraft AI uses a dedicated knowledge base containing resume and ATS
guidance.

``` text
data/knowledge/
│
├── ats_guidelines.txt
├── bullet_writing.txt
└── resume_guidelines.txt
```

The pipeline is:

``` text
Knowledge Documents
        ↓
Document Chunking
        ↓
Sentence Transformer Embeddings
        ↓
ChromaDB
        ↓
Similarity Retrieval
        ↓
Relevant Guidance
        ↓
Groq LLM
        ↓
Grounded Generation
```

The retrieved source information is also surfaced in the application so
that the user can understand what guidance contributed to the generated
recommendations.

------------------------------------------------------------------------

## 🧪 Evaluation

The project includes an evaluation pipeline for measuring resume/job
matching behavior.

Evaluation resources can be obtained using:

``` bash
python scripts/download_kaggle_data.py
```

Run the evaluation with:

``` bash
python scripts/run_evaluation.py
```

The evaluation layer is designed to measure aspects such as:

-   Classification/label accuracy
-   Required-skill coverage
-   Resume/JD matching behavior

The project uses external datasets primarily for **benchmarking and
evaluation**, rather than training a custom foundation model.

------------------------------------------------------------------------

## 🛠️ Technology Stack

### Generative AI

-   Groq
-   Large Language Models
-   LangChain
-   Prompt engineering
-   Pydantic structured outputs

### Retrieval

-   Sentence Transformers
-   ChromaDB
-   Semantic similarity search
-   RAG

### Backend

-   Python
-   FastAPI
-   REST APIs
-   Pydantic
-   SQLite

### Frontend

-   Streamlit
-   Custom CSS

### Engineering

-   Docker
-   Pytest
-   Git / GitHub
-   Environment-based configuration

------------------------------------------------------------------------

## 🎨 UI / UX

The application's UI was designed specifically for CareerCraft AI with a
focus on:

-   Clean dark interface
-   Interactive analysis dashboard
-   Metric cards
-   Skill pills
-   Progress indicators
-   Result tabs
-   Expandable interview sections
-   Export controls
-   Responsive Streamlit layout
-   Lightweight animations and visual feedback

### UI development disclosure

> **The UI/UX implementation was developed with assistance from
> ChatGPT.**

------------------------------------------------------------------------

## ⚙️ Local Setup

### 1. Clone the repository

``` bash
git clone https://github.com/<your-username>/CareerCraft-AI.git
cd CareerCraft-AI
```

### 2. Create a virtual environment

Windows:

``` bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` from `.env.example`.

``` env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b

LANGSMITH_API_KEY=
LANGSMITH_TRACING=false

BACKEND_URL=http://localhost:8000
MAX_FILE_SIZE_MB=5
CORS_ORIGINS=http://localhost:8501
RAG_ENABLED=true
```

**Never commit `.env` or API keys to GitHub.**

### 5. Build the RAG knowledge index

``` bash
python -m scripts.ingest_knowledge
```

### 6. Start the FastAPI backend

``` bash
uvicorn backend.main:app --reload --port 8000
```

### 7. Start the Streamlit application

Open another terminal:

``` bash
streamlit run app/streamlit_app.py
```

Open:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

## 🐳 Docker

Build and run the project using:

``` bash
docker compose up --build
```

The exact environment variables required by the application should be
configured through the environment or an appropriate `.env` file that is
kept out of version control.

------------------------------------------------------------------------

## 📌 API Endpoints

The FastAPI backend exposes the following endpoints:

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Application information |
| `/health` | GET | Backend health check |
| `/rag/status` | GET | Check RAG system status |
| `/rag/ingest` | POST | Rebuild the RAG knowledge index |
| `/parse-resume` | POST | Parse an uploaded resume |
| `/analyze` | POST | Perform complete resume/JD analysis |
| `/history` | GET | Retrieve previous analyses |
| `/export/resume` | POST | Export tailored resume |
| `/export/cover-letter` | POST | Export generated cover letter |
| `/export/report` | POST | Export analysis report |
| `/evaluation` | GET | Retrieve evaluation metrics |

------------------------------------------------------------------------

## 📈 Example Workflow

``` text
Upload Resume
      │
      ▼
Paste Job Description
      │
      ▼
┌───────────────────────┐
│ Resume Understanding  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Job Understanding     │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Resume ↔ Job Matching │
└───────────┬───────────┘
            │
      ┌─────┴─────┐
      ▼           ▼
 Skill Gaps      RAG
      │           │
      └─────┬─────┘
            ▼
      Generative AI
            │
      ┌─────┼─────────┐
      ▼     ▼         ▼
   Resume  Cover    Interview
   Update  Letter    Prep
            │
            ▼
       Quality Check
            │
            ▼
          Export
```

------------------------------------------------------------------------

## 👨‍💻 Author
### Khushaan Saini

**B.E. Electronics & Computer Engineering**\
Thapar Institute of Engineering & Technology

Generative AI • RAG • Python • FastAPI • LangChain • Machine Learning
