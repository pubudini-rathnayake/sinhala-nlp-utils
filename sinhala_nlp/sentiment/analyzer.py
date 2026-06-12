import re
from typing import Dict

# Rule-based positive/negative word lists (expandable)
POSITIVE_WORDS = {
    "හොඳ", "ලස්සන", "සතුටු", "සාර්ථක", "ප්‍රිය", "විශිෂ්ට",
    "good", "great", "happy", "excellent", "wonderful", "love", "nice"
}

NEGATIVE_WORDS = {
    "නරක", "දුක", "කණගාටු", "අසාර්ථක", "ප්‍රශ්නය", "කෝප",
    "bad", "sad", "terrible", "awful", "hate", "poor", "worst"
}

def analyze_sentiment(text: str) -> Dict[str, object]:
    """
    Rule-based sentiment analysis for Sinhala/English text.

    Returns a dict with keys:
        label  — 'positive', 'negative', or 'neutral'
        score  — float from -1.0 (most negative) to +1.0 (most positive)
        counts — breakdown of matched positive/negative words
    """
    words = re.findall(r"[\u0D80-\u0DFF]+|[a-zA-Z]+", text.lower())
    pos = sum(1 for w in words if w in POSITIVE_WORDS)
    neg = sum(1 for w in words if w in NEGATIVE_WORDS)
    total = pos + neg

    if total == 0:
        score = 0.0
        label = "neutral"
    else:
        score = round((pos - neg) / total, 4)
        label = "positive" if score > 0 else "negative" if score < 0 else "neutral"

    return {"label": label, "score": score, "counts": {"positive": pos, "negative": neg}}