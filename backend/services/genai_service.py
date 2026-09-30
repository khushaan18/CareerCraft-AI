from ..llm import get_llm
from ..prompts import *
from ..schemas.models import *
from .matching_service import match_resume
from .rag_service import retrieve_with_sources


def invoke(schema, prompt):
    return get_llm().with_structured_output(
        schema,
        method="json_schema",
        strict=False
    ).invoke(prompt)


def analyze_resume(text):
    return invoke(ResumeProfile, RESUME_PROMPT.format(resume_text=text))


def analyze_jd(text):
    return invoke(JobProfile, JD_PROMPT.format(job_description=text))


def generate_analysis(resume_text, jd_text):
    # 1. Structured extraction
    r = analyze_resume(resume_text)
    j = analyze_jd(jd_text)

    # 2. Deterministic semantic/keyword matching
    m = MatchResult(**match_resume(r, j))
    gap = SkillGapResult(
        strong=m.matched_skills,
        partial=m.partial_matches,
        missing=m.missing_skills,
        learning_priorities=m.missing_skills[:5],
    )

    # 3. RAG: retrieve relevant ATS/resume-writing guidance using the actual job context
    query = (
        f"Resume optimization and ATS guidance for {j.title or 'this role'}. "
        f"Required skills: {', '.join(j.required_skills)}. "
        f"Keywords: {', '.join(j.keywords)}. "
        f"Missing skills: {', '.join(m.missing_skills)}."
    )
    retrieved = retrieve_with_sources(query)
    guidance = [item["content"] for item in retrieved]
    rag_sources = sorted(set(item["source"] for item in retrieved))
    rag_context = "\n\n".join(guidance) or "No knowledge-base guidance was retrieved."

    # 4. Generation grounded by both resume/JD facts and retrieved guidance
    o = invoke(
        OptimizedResume,
        OPTIMIZE_PROMPT.format(
            resume_json=r.model_dump_json(),
            job_json=j.model_dump_json(),
            guidance=rag_context,
        ),
    )
    c = invoke(
        CoverLetter,
        COVER_PROMPT.format(
            resume_json=r.model_dump_json(),
            job_json=j.model_dump_json(),
            guidance=rag_context,
        ),
    )
    a = invoke(
        ATSAnalysis,
        ATS_PROMPT.format(
            resume_json=r.model_dump_json(),
            job_json=j.model_dump_json(),
            guidance=rag_context,
        ),
    )
    q = invoke(
        InterviewQuestions,
        INTERVIEW_PROMPT.format(
            resume_json=r.model_dump_json(),
            job_json=j.model_dump_json(),
            guidance=rag_context,
        ),
    )
    quality = invoke(
        QualityResult,
        QUALITY_PROMPT.format(
            resume_json=r.model_dump_json(),
            optimized_json=o.model_dump_json(),
            cover_letter_json=c.model_dump_json(),
        ),
    )

    return AnalysisResponse(
        resume=r,
        job=j,
        match=m,
        ats=a,
        skill_gap=gap,
        optimized_resume=o,
        cover_letter=c,
        interview_questions=q,
        quality=quality,
        retrieved_guidance=guidance,
        rag_sources=rag_sources,
    )
