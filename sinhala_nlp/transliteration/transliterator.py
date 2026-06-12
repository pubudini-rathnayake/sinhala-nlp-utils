# Singlish (Roman) → Sinhala Unicode mapping
SINGLISH_TO_SINHALA = {
    "a": "අ", "aa": "ආ", "i": "ඉ", "ii": "ඊ", "u": "උ", "uu": "ඌ",
    "e": "එ", "ee": "ඒ", "o": "ඔ", "oo": "ඕ", "au": "ඖ", "ai": "ඓ",
    "k": "ක", "g": "ග", "t": "ට", "d": "ඩ", "n": "න", "p": "ප",
    "b": "බ", "m": "ම", "y": "ය", "r": "ර", "l": "ල", "w": "ව",
    "s": "ස", "h": "හ", "f": "ෆ",
}

SINHALA_TO_SINGLISH = {v: k for k, v in SINGLISH_TO_SINHALA.items()}

def to_singlish(text: str) -> str:
    """Convert Sinhala Unicode text to approximate Singlish (Roman) representation."""
    result = []
    for char in text:
        result.append(SINHALA_TO_SINGLISH.get(char, char))
    return "".join(result)

def to_sinhala(text: str) -> str:
    """Convert Singlish (Roman) text to Sinhala Unicode (best-effort)."""
    result = []
    i = 0
    text = text.lower()
    while i < len(text):
        # Try two-char match first
        if i + 1 < len(text) and text[i:i+2] in SINGLISH_TO_SINHALA:
            result.append(SINGLISH_TO_SINHALA[text[i:i+2]])
            i += 2
        elif text[i] in SINGLISH_TO_SINHALA:
            result.append(SINGLISH_TO_SINHALA[text[i]])
            i += 1
        else:
            result.append(text[i])
            i += 1
    return "".join(result)