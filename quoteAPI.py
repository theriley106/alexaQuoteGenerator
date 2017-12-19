from bs4 import BeautifulSoup
import requests
import random
import os
import os.path

popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love']

def writeQuoteList(author,quoteList):
    f = open('{}.txt'.format(author),'w')
    f.write('\n'.join(quoteList))
    f.close()

def readData(author):
    return open('{}.txt'.format(author)).read().split('\n')


def get_author_quotes(author, forceNew=False):
    quotes = []
    author = str(author.strip()).replace(' ', '_')
    if os.path.exists('{}.txt'.format(author)) == False or forceNew == True:
        url = "http://www.brainyquote.com/quotes/authors/{}".format(author)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        for quote in soup.select('.b-qt'):
            quotes.append(quote.getText())
        if len(quotes) > 3:
            writeQuoteList(author,quotes)
    else:
        quotes = readData(author)
    return random.choice(quotes)


def get_quotes(type, number_of_quotes=1):
    url = "http://www.brainyquote.com/quotes/authors/elon_musk"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = []
    for quote in soup.select('.b-qt'):
        quotes.append(quote.getText())
    random.shuffle(quotes)
    result = quotes[:number_of_quotes]
    return result


def get_random_quote():
    result = get_quotes(popular_choice[random.randint(0, len(popular_choice) - 1)])
    return result

#print get_author_quotes('bill gates')

#print get_quotes('type', number_of_quotes=100)