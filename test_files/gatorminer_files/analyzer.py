"""Text Proprocessing."""
from collections import Counter
from textblob import TextBlob
import pandas as pd
import re
import string
from typing import List, Tuple
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from . import markdown as md

PARSER = spacy.load("en_core_web_sm")


def normalize(data: str) -> str:
    """Remove numbers and to lowercase."""
    data = data.lower()
    # remove number
    # using a list in case more regex are needed
    regex_lst = [r"\b[0-9]+\b", r"\W+"]
    generic_re = "|".join(regex_lst)
    normal_text = re.sub(rf"{generic_re}", " ", data)
    spacefree_text = re.sub(r"\s{1,}", " ", normal_text)
    return spacefree_text


def lemmatized_text(text):
    """Return lemmatized text."""
    tokens = PARSER(text)
    tokens = [
        word.lemma_.strip()
        for word in tokens if word.lemma_ != "-PRON-"
    ]
    lem_text = " ".join(tokens)
    return lem_text


def tokenize(normalized_text: str) -> List[str]:
    """Break down text into a list of lemmatized tokens."""
    # remove punctuation
    normal_text = "".join(
        c for c in normalized_text if c not in string.punctuation
    )
    tokens = PARSER(normal_text)
    # lemmatize tokens, remove pronoun and stop words
    tokens = [
        word.lemma_.strip()
        for word in tokens
        if word.lemma_ != "-PRON-"
        and word.is_stop is False
        and len(word.lemma_.strip()) > 1
    ]
    return tokens


def compute_frequency(
        token_lst: List[str], amount=50
) -> List[Tuple[str, int]]:  # noqa: E501
    """Compute word frequency from a list of tokens."""
    word_freq = Counter(token_lst)
    return word_freq.most_common(amount)


def word_frequency(text: str, amount=50) -> List[Tuple[str, int]]:
    """Pipeline to normalize, tokenize, and find word frequency of raw text."""
    return compute_frequency(tokenize(normalize(text)), amount)


def dir_frequency(dirname: str, amount=50) -> List[Tuple[str, int]]:
    """Pipeline of word_frequency from a directory of raw input file."""
    md_list = md.collect_md_text(dirname)
    return compute_frequency(tokenize(normalize(" ".join(md_list))), amount)


def sentence_tokenize(input_text):
    """Tokenize paragraph to a list of sentences."""
    sent_lst = []
    sent_pipe = PARSER.create_pipe("sentencizer")
    PARSER.add_pipe(sent_pipe)
    doc = PARSER(input_text)
    for sent in doc.sents:
        sent_lst.append(sent.text)
    return sent_lst


def part_of_speech(input_text):
    """Part of speech tagging of sentence."""
    doc = PARSER(input_text)
    pos_lst = []
    for word in doc:
        pos_lst.append((word.text, word.pos_))
    return pos_lst


def compute_tfidf(data: List[str]) -> None:
    """Compute the TFIDF."""
    tfidf_vectorizer = TfidfVectorizer()
    # make data iterable for TFIDF
    tfs = tfidf_vectorizer.fit_transform([" ".join(data)])
    feature_names = tfidf_vectorizer.get_feature_names()
    for col in tfs.nonzero()[1]:
        print(feature_names[col], " - ", tfs[0, col])
    return tfs, tfidf_vectorizer


def compute_count_vectorize(data):
    """Compute the count vectorize matrix."""
    count_vectorizer = CountVectorizer()
    count = count_vectorizer.fit_transform(data)
    return count, count_vectorizer


def named_entity_recognization(input_text):
    """Named entity within an input string of text."""
    doc = PARSER(input_text)
    ent_lst = []
    for entity in doc.ents:
        print(entity, entity.label_)
        ent_lst.append((str(entity), entity.label_))
    # spacy.displacy.serve(doc, style="ent")
    # display in jupyter notebook
    # displacy.render(about_interest_doc, style='dep', jupyter=True)
    return ent_lst


def get_nlp(input_text):
    """Return the spacy nlp object."""
    doc = PARSER(input_text)
    return doc


def noun_phrase(input_text):
    """Extract noun phrases of the document in a list."""
    doc = PARSER(input_text)
    n_phrase_lst = []
    for chunk in doc.noun_chunks:
        n_phrase_lst.append(str(chunk))
    return n_phrase_lst


def top_polarized_word(tokens_column):
    """Create columns for positive and negative words."""
    # Start off with empty lists
    pos_series = []
    neg_series = []
    # For each item in the already existing tokens column in the data frame,
    for token_element in tokens_column:
        words = sorted_sentiment_word_list(token_element)
        # Add the words at the end of the list to the display series since
        # they have the most positive sentiment value
        pos_series.append(", ".join(words[::-1][0:3]))
        neg_series.append(", ".join(words[0:3]))
    # Return an entire series based on the display_series list
    return pd.Series(pos_series), pd.Series(neg_series)


def sorted_sentiment_word_list(token_element):
    """Creates and sorts a word list from a list of tokens."""
    # Convert the token list into a set so that it only has the unique words
    words = set(token_element)
    # Convert back into list to iterate through
    unique_words = list(words)
    # Returning the sorted list
    return sorted(unique_words, key=lambda x: TextBlob(x).sentiment.polarity)