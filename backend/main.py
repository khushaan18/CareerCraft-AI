import traceback
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from .config import CORS_ORIGINS,MAX_FILE_SIZE_MB
from .parsers.document_parser import extract_text
from .services.genai_service import generate_analysis
from .services.history import init_db,save_analysis,list_history
from .services.exporter import resume_docx,cover_docx,report_pdf
from .schemas.models import AnalysisResponse
from .services.rag_service import status as rag_status, build_index
from evaluation.evaluator import run as evaluation_run, dataset_status

app=FastAPI(title="CareerCraft AI API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=CORS_ORIGINS,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
init_db()

@app.get("/")
def root():return {"name":"CareerCraft AI","type":"Generative AI Resume Assistant"}
@app.get("/health")
def health():return {"status":"ok", "rag": rag_status()}

@app.get("/rag/status")
def rag_health():
    return rag_status()

@app.post("/rag/ingest")
def rag_ingest():
    chunks = build_index(force=True)
    return {"status":"indexed", "chunks":chunks, "rag":rag_status()}

@app.get("/evaluation")
def evaluation():
    return {"metrics": evaluation_run(), "datasets": dataset_status()}

@app.post("/parse-resume")
async def parse_resume(file:UploadFile=File(...)):
    data=await file.read()
    if len(data)>MAX_FILE_SIZE_MB*1024*1024:raise HTTPException(413,"File is too large.")
    try:return {"text":extract_text(file.filename,data)}
    except ValueError as e:raise HTTPException(400,str(e))

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    if not job_description.strip():
        raise HTTPException(400, "job_description is required.")

    data = await file.read()

    if len(data) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(413, "File is too large.")

    try:
        x = generate_analysis(
            extract_text(file.filename, data),
            job_description
        )

        save_analysis(x)

        return x.model_dump()

    except Exception as e:
        print("\n" + "=" * 80)
        print("ANALYZE ERROR")
        print("=" * 80)
        traceback.print_exc()
        print("=" * 80 + "\n")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
@app.get("/history")
def history():return list_history()

def export(payload,fn,mime,content):
    x=AnalysisResponse(**payload)
    return Response(content(x),media_type=mime,headers={"Content-Disposition":f"attachment; filename={fn}"})

@app.post("/export/resume")
def exp_resume(payload:dict):return export(payload,"CareerCraft_Resume.docx","application/vnd.openxmlformats-officedocument.wordprocessingml.document",resume_docx)
@app.post("/export/cover-letter")
def exp_cover(payload:dict):return export(payload,"CareerCraft_Cover_Letter.docx","application/vnd.openxmlformats-officedocument.wordprocessingml.document",cover_docx)
@app.post("/export/report")
def exp_report(payload:dict):return export(payload,"CareerCraft_Report.pdf","application/pdf",report_pdf)
