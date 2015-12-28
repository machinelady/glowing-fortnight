import itertools
import nltk
from nltk.corpus import gutenberg, stopwords
import re
import random

# Project Gutenberg books that I'm using for quotes at the moment
books = [u'austen-emma.txt', u'austen-persuasion.txt', u'austen-sense.txt', u'blake-poems.txt', u'bryant-stories.txt', u'burgess-busterbrown.txt', u'carroll-alice.txt', u'chesterton-ball.txt', u'chesterton-brown.txt', u'chesterton-thursday.txt', u'edgeworth-parents.txt', u'melville-moby_dick.txt', u'milton-paradise.txt', u'whitman-leaves.txt']

def cleanup_text(strings):
    """
        strings: a list of words and punctuation, as returned by nltk's corpus.gutenberg.sents()

        Returns a human-readable sentence, with correct spacing around punctuation.
    """
    sentence = " ".join(strings)
    sentence = re.sub(r'\\', '', sentence)
    # strip out spaces in front of punctuations
    return re.sub(r'\s([;:?,.!"\'](?:\s|$))', r'\1', sentence)

def is_tweetable(sentence):
    """
    Checks if a sentence is of the correct length to tweet it. We don't want sentences that are too short (e.g. just "Yes, that's right"),
    or sentences that will be too long for a single tweet.
    """
    return 40 < len(cleanup_text(sentence)) < 100

def sentences_with_sources(books):
    for book in books:
        for sentence in gutenberg.sents(book):
            yield sentence, book


def find_potential_topics(sentence):
    """
    sentence: a list of words/punctuation as returned by gutenberg.sents

    First pass: Remove stopwords
    """
    def is_word(w):
        return re.match('\w+', w)

    no_stopwords = [word for word in sentence if word not in stopwords.words('english') and is_word(word)]
    
    return no_stopwords


def find_tweetable_sentences(corpus):
    """
    Finds tweetable sentences in a corpus.
    """
    return [{'quote': cleanup_text(sent), 'source': source, 'potential_topics': find_potential_topics(sent)} for sent, source in corpus if is_tweetable(sent)]

tweetable_sentences = find_tweetable_sentences(sentences_with_sources(books))

def find_matching(keywords):
    pass


def random_sentence():
    return random.choice(tweetable_sentences)


