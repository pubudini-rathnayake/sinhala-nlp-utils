import re
from typing import List

SENTENCE_ENDINGS = re.compile(r"(?<=[^\s])[.!?෴།\n](?=\s|$)")
SINHALA_CHAR = re.compile(r"[\u0D80-\u0DFF]")

def word_tokenize(text: str, keep_punctuation=False) -> List[str]:
    raw_tokens = text.strip().split()
    tokens = []
    punct = re.compile(r"([!\"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~෴།])")
    for token in raw_tokens:
        for part in punct.split(token):
            part = part.strip()
            if not part:
                continue
            if punct.fullmatch(part):
                if keep_punctuation:
                    tokens.append(part)
            else:
                tokens.append(part)
    return tokens

def sentence_tokenize(text: str) -> List[str]:
    return [s.strip() for s in SENTENCE_ENDINGS.split(text.strip()) if s.strip()]

def char_tokenize(text: str, sinhala_only=False) -> List[str]:
    if sinhala_only:
        return [c for c in text if SINHALA_CHAR.match(c)]
    return list(text)