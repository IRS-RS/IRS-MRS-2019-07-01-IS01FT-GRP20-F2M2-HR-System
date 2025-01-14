import re
import unicodedata

import inflect
from autocorrect import spell
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)


def denoise_text(text):
    text = remove_between_square_brackets(text)
    return text


def spellCorrect(words):
    correctWords = []
    for i in words:
        correctWords.append(spell(i))
    return " ".join(correctWords)

def remove_non_ascii(words):
#Remove non-ASCII characters from list of tokenized words
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def replace_numbers(string):
    # Replace all integer occurrences in string with textual representation
    words = string.split(" ")
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return " ".join(new_words)


def remove_stopwords(words):
#Remove stop words from list of tokenized words
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(words)
    result = [i for i in tokens if not i in stop_words]
    return result


def stem_words(words):
#Stem words in list of tokenized words
    stemmer = PorterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems


def lemmatize_verbs(words):
#Lemmatize verbs in list of tokenized words
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

