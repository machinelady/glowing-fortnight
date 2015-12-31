import pictures

import quotes

if __name__ == '__main__':
    random_quote = quotes.random_sentence()
    text = random_quote["quote"]
    topics = random_quote["potential_topics"]

    link = pictures.find_picture("cat", topics)
    tweet = '"{}" {} {}'.format(text, link)
    print tweet
