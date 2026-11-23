# LK sinhala-nlp-utils

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![NLP](https://img.shields.io/badge/NLP-Sinhala-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A lightweight, dependency-free Python toolkit for **Sinhala Natural Language Processing**.
Supports mixed Sinhala/English text — built for real-world Sri Lankan data.

## ✨ Features

| Module | Description |
|---|---|
| `preprocessing` | Clean, normalize, and de-noise Sinhala/English text |
| `tokenization` | Word, sentence, character, and n-gram tokenization |
| `transliteration` | Sinhala ↔ Singlish (Roman) script conversion |
| `sentiment` | Rule-based sentiment analysis (positive / negative / neutral) |
| `detection` | Detect whether text is Sinhala, English, or Mixed |

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/sinhala-nlp-utils.git
cd sinhala-nlp-utils
pip install -e .
```

```python
from sinhala_nlp import clean_text, word_tokenize, detect_language, analyze_sentiment

text = "ශ්‍රී ලංකාව ලස්සන රටකි! 😊 https://example.com"

print(clean_text(text, remove_punctuation=True))
# → ශ්‍රී ලංකාව ලස්සන රටකි 😊

print(word_tokenize("මම ගෙදර යනවා."))
# → ['මම', 'ගෙදර', 'යනවා']

print(detect_language("ශ්‍රී ලංකාව ලස්සන රටකි"))
# → {'language': 'sinhala', 'sinhala_ratio': 0.95, 'english_ratio': 0.0}

print(analyze_sentiment("This is a good result"))
# → {'label': 'positive', 'score': 1.0, 'counts': {'positive': 1, 'negative': 0}}
```

## 📁 Project Structure

```
sinhala-nlp-utils/
├── sinhala_nlp/
│   ├── preprocessing/    # clean_text, normalize_text, remove_noise
│   ├── tokenization/     # word_tokenize, sentence_tokenize, char_tokenize
│   ├── transliteration/  # to_singlish, to_sinhala
│   ├── sentiment/        # analyze_sentiment
│   └── detection/        # detect_language
├── notebooks/            # Interactive demos
├── data/sample/          # Sample Sinhala texts
└── tests/                # Unit tests
```

## 🗺️ Roadmap

- [ ] Expand sentiment word lists
- [ ] Add stopword removal
- [ ] Gemini API integration for advanced analysis
- [ ] Publish to PyPI

