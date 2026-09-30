from backend.schemas.models import ResumeProfile,JobProfile

def test_models():
    assert ResumeProfile().skills.technical == []
    assert JobProfile().required_skills == []
