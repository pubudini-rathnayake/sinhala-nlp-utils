from sinhala_nlp.preprocessing.cleaner import clean_text, normalize_text
from sinhala_nlp.tokenization.tokenizer import word_tokenize, sentence_tokenize
from sinhala_nlp.transliteration.transliterator import to_singlish, to_sinhala
from sinhala_nlp.sentiment.analyzer import analyze_sentiment
from sinhala_nlp.detection.detector import detect_language

__version__ = "0.1.0"
__author__ = "Pubudini"