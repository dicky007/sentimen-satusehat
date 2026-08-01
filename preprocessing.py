import re
import os
from textblob import TextBlob
import nltk
import streamlit as st
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory



# Mengunduh resource NLTK yang dibutuhkan TextBlob / Tokenizer
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/brown')
except LookupError:
    nltk.download('brown')

# Jika butuh stopwords atau resource lain, tambahkan juga di sini:
nltk.download('stopwords')
nltk.download('wordnet')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NLTK_DATA_DIR = os.path.join(BASE_DIR, 'nltk_data')

if NLTK_DATA_DIR not in nltk.data.path:
    nltk.data.path.append(NLTK_DATA_DIR)

@st.cache_resource
def load_nlp_resources():
    stemmer = StemmerFactory().create_stemmer()
    stopword_remover = StopWordRemoverFactory().create_stop_word_remover()
    return stemmer, stopword_remover

stemmer, stopword_remover = load_nlp_resources()

def normalize_slang(text, slang_dict):
    wordlist = TextBlob(text).words
    normalized_words = []
    for word in wordlist:
        if word in slang_dict:
            normalized_words.append(slang_dict[word])
        else:
            normalized_words.append(word)
    return ' '.join(normalized_words)

def preprocess_text(text, slang_dict):
    text = text.lower()
    text = re.sub(r'@[A-Za-z0-9_]+','', text)
    text = re.sub(r'#\w+','', text)
    text = re.sub(r'RT[\s]','', text)
    text = re.sub(r'https?://\S+','', text)
    text = re.sub(r'r\$\w*', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[0-9]+', '', text)
    text = re.sub(r'[^A-Za-z0-9 ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'(.)\1+', r'\1\1', text)

    text = normalize_slang(text, slang_dict)
    text = stopword_remover.remove(text)
    text = stemmer.stem(text)
    return text
