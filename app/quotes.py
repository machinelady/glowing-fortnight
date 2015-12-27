import itertools
import nltk
from nltk.corpus import gutenberg
import re
import random

def cleanup_text(strings):
    sentence = " ".join(strings)
    sentence = re.sub(r'\\', '', sentence)
    # strip out spaces in front of punctuations
    return re.sub(r'\s([;:?,.!"\'](?:\s|$))', r'\1', sentence)

def is_tweetable(sentence):
    return 40 < len(cleanup_text(sentence)) < 100

def sentences_with_sources(books):
    for book in books:
        for sentence in gutenberg.sents(book):
            yield sentence, book

def find_tweetable_sentences():
    books = [u'austen-emma.txt', u'austen-persuasion.txt', u'austen-sense.txt', u'blake-poems.txt', u'bryant-stories.txt', u'burgess-busterbrown.txt', u'carroll-alice.txt', u'chesterton-ball.txt', u'chesterton-brown.txt', u'chesterton-thursday.txt', u'edgeworth-parents.txt', u'melville-moby_dick.txt', u'milton-paradise.txt', u'whitman-leaves.txt']
    return [{'quote': cleanup_text(sent), 'source': source} for sent, source in sentences_with_sources(books) if is_tweetable(sent)]

tweetable_sentences = find_tweetable_sentences()

def find_matching(keywords):
    pass


def random_sentence():
    return random.choice(tweetable_sentences)
