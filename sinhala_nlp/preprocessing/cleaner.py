import re
import unicodedata

SINHALA_RANGE = re.compile(r"[\u0D80-\u0DFF]")

def clean_text(text, remove_english=False, remove_numbers=False, remove_punctuation=False):
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"\s+", " ", text).strip()
    if remove_english:
        text = re.sub(r"[a-zA-Z]+", "", text)
    if remove_numbers:
        text = re.sub(r"[0-9\u0DE6-\u0DEF]+", "", text)
    if remove_punctuation:
        text = re.sub(r"[!\"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]", "", text)
    return re.sub(r"\s+", " ", text).strip()

def normalize_text(text):
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\u200B", "").replace("\uFEFF", "")
    return text.strip()

def remove_noise(text):
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"[@#]\w+", "", text)
    text = re.sub(r"[!?.]{2,}", ".", text)
    return re.sub(r"\s+", " ", text).strip()

def is_sinhala(text, threshold=0.5):
    chars = [c for c in text if not c.isspace()]
    if not chars:
        return False
    sinhala_chars = [c for c in chars if SINHALA_RANGE.match(c)]
    return len(sinhala_chars) / len(chars) >= threshold