from functools import lru_cache
from ..utils.text import normalize,keyword_coverage

@lru_cache(maxsize=1)
def model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("all-MiniLM-L6-v2")

def resume_text(r):
    out=[r.summary," ".join(r.skills.technical+r.skills.tools+r.skills.soft)]
    for x in r.experience: out.append(x.role+" "+x.company+" "+" ".join(x.bullets))
    for x in r.projects: out.append(x.name+" "+x.description+" "+" ".join(x.technologies+x.bullets))
    return " ".join(out)

def match_resume(r,j):
    src=resume_text(r); s=normalize(src); req=list(dict.fromkeys(j.required_skills+j.preferred_skills))
    matched=[x for x in req if normalize(x) in s]; missing=[x for x in req if normalize(x) not in s]
    cov=keyword_coverage(src,j.keywords)
    try:
        m=model(); e=m.encode([src," ".join(req+j.responsibilities)],normalize_embeddings=True); sim=max(0,float(e[0]@e[1]))
    except Exception: sim=0
    score=round(max(0,min(100,cov*70+sim*30)))
    return {"alignment_score":score,"matched_skills":matched,"partial_matches":missing[:3],"missing_skills":missing[3:],
            "matched_keywords":[k for k in j.keywords if normalize(k) in s],
            "missing_keywords":[k for k in j.keywords if normalize(k) not in s],
            "explanation":f"Heuristic score combines keyword coverage ({cov:.0%}) and semantic similarity ({sim:.2f}); it is not a proprietary ATS score."}
