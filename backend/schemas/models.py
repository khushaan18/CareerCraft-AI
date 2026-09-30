from typing import List
from pydantic import BaseModel,Field

class PersonalInformation(BaseModel):
    name:str=""; email:str=""; phone:str=""; location:str=""; linkedin:str=""; github:str=""
class Education(BaseModel):
    institution:str=""; degree:str=""; field:str=""; start_date:str=""; end_date:str=""; details:List[str]=Field(default_factory=list)
class Experience(BaseModel):
    company:str=""; role:str=""; start_date:str=""; end_date:str=""; bullets:List[str]=Field(default_factory=list)
class Project(BaseModel):
    name:str=""; description:str=""; technologies:List[str]=Field(default_factory=list); bullets:List[str]=Field(default_factory=list)
class Skills(BaseModel):
    technical:List[str]=Field(default_factory=list); tools:List[str]=Field(default_factory=list); soft:List[str]=Field(default_factory=list)
class ResumeProfile(BaseModel):
    personal:PersonalInformation=Field(default_factory=PersonalInformation); summary:str=""
    education:List[Education]=Field(default_factory=list); experience:List[Experience]=Field(default_factory=list)
    projects:List[Project]=Field(default_factory=list); skills:Skills=Field(default_factory=Skills); certifications:List[str]=Field(default_factory=list)
class JobProfile(BaseModel):
    title:str=""; company:str=""; required_skills:List[str]=Field(default_factory=list); preferred_skills:List[str]=Field(default_factory=list)
    responsibilities:List[str]=Field(default_factory=list); qualifications:List[str]=Field(default_factory=list); keywords:List[str]=Field(default_factory=list)
class MatchResult(BaseModel):
    alignment_score:int=0; matched_skills:List[str]=Field(default_factory=list); partial_matches:List[str]=Field(default_factory=list)
    missing_skills:List[str]=Field(default_factory=list); matched_keywords:List[str]=Field(default_factory=list); missing_keywords:List[str]=Field(default_factory=list); explanation:str=""
class ATSAnalysis(BaseModel):
    estimated_score:int=0; strengths:List[str]=Field(default_factory=list); issues:List[str]=Field(default_factory=list)
    keyword_suggestions:List[str]=Field(default_factory=list); formatting_suggestions:List[str]=Field(default_factory=list); notes:str=""
class SkillGapResult(BaseModel):
    strong:List[str]=Field(default_factory=list); partial:List[str]=Field(default_factory=list); missing:List[str]=Field(default_factory=list); learning_priorities:List[str]=Field(default_factory=list)
class OptimizedResume(BaseModel):
    summary:str=""; improved_bullets:List[str]=Field(default_factory=list); suggested_changes:List[str]=Field(default_factory=list)
class CoverLetter(BaseModel):
    subject:str=""; body:str=""
class InterviewQuestions(BaseModel):
    technical:List[str]=Field(default_factory=list); resume_based:List[str]=Field(default_factory=list); behavioral:List[str]=Field(default_factory=list)
class QualityResult(BaseModel):
    unsupported_claims:List[str]=Field(default_factory=list); potential_inventions:List[str]=Field(default_factory=list); consistency_issues:List[str]=Field(default_factory=list); safe_to_use:bool=True
class AnalysisResponse(BaseModel):
    resume:ResumeProfile; job:JobProfile; match:MatchResult; ats:ATSAnalysis; skill_gap:SkillGapResult
    optimized_resume:OptimizedResume; cover_letter:CoverLetter; interview_questions:InterviewQuestions; quality:QualityResult
    retrieved_guidance:List[str]=Field(default_factory=list)
    rag_sources:List[str]=Field(default_factory=list)
