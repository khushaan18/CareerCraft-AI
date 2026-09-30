from backend.utils.text import keyword_coverage

def test_keyword_coverage():
    assert keyword_coverage('Python FastAPI SQL',['Python','SQL']) == 1.0
