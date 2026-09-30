from backend.parsers.document_parser import extract_text

def test_txt_parser():
    assert 'Python' in extract_text('resume.txt',b'Python developer')
