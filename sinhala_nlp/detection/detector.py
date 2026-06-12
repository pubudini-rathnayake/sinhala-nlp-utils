import re
from typing import Dict

SINHALA_RE = re.compile(r"[\u0D80-\u0DFF]")
LATIN_RE = re.compile(r"[a-zA-Z]")

def detect_language(text: str) -> Dict[str, object]:
    """
    Detect whether text is Sinhala, English, or Mixed.

    Returns:
        dict with keys: language, sinhala_ratio, english_ratio
    """
    chars = [c for c in text if not c.isspace()]
    if not chars:
        return {"language": "unknown", "sinhala_ratio": 0.0, "english_ratio": 0.0}

    sinhala = sum(1 for c in chars if SINHALA_RE.match(c))
    english = sum(1 for c in chars if LATIN_RE.match(c))
    total = len(chars)

    s_ratio = round(sinhala / total, 4)
    e_ratio = round(english / total, 4)

    if s_ratio >= 0.7:
        lang = "sinhala"
    elif e_ratio >= 0.7:
        lang = "english"
    elif s_ratio > 0.1 and e_ratio > 0.1:
        lang = "mixed"
    else:
        lang = "unknown"

    return {"language": lang, "sinhala_ratio": s_ratio, "english_ratio": e_ratio}