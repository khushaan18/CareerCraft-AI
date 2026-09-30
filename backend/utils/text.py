import re
def normalize(text): return re.sub(r"\s+"," ",text.lower()).strip()
def keyword_coverage(source,keywords):
    if not keywords:return 0.0
    s=normalize(source); return sum(normalize(k) in s for k in keywords)/len(keywords)
