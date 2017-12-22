from bs4 import BeautifulSoup
import requests
import random
import os
import os.path
import updateAfterIntent
import time

popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love']

def fileOlderThan(fileName, day=1):
	current_time = time.time()
	creation_time = os.path.getctime(fileName)
	if (current_time - creation_time) // (24 * 3600) >= day:
		return True
	else:
		return False


def writeQuoteList(author,quoteList):
	f = open('/tmp/{}.txt'.format(author),'w')
	print("wrote to {}.txt".format(author))
	f.write('\n'.join(quoteList))
	f.close()

def readData(author):
	return open('/tmp/{}.txt'.format(author)).read().split('\n')


def get_author_quotes(author, forceNew=False):
	author = str(author.strip()).replace(' ', '_')
	if os.path.exists('/tmp/{}.txt'.format(author)) == False or forceNew == True:
		quotes = updateAfterIntent.checkForUpdateOnGithub(author)
		if quotes == None:
			quotes = []
			url = "http://www.brainyquote.com/quotes/authors/{}".format(author)
			response = requests.get(url)
			soup = BeautifulSoup(response.text, "lxml")
			for quote in soup.select('.b-qt'):
				quotes.append(quote.getText())
			print("Grabbed New Quotes from Brainy Quote")
		if len(quotes) > 2:
			writeQuoteList(author,quotes)
			
	else:
		quotes = readData(author)
		print("Read quotes from local file")
		if fileOlderThan('/tmp/{}.txt'.format(author)) == True:
			print("File is older...")
			newData = updateAfterIntent.checkForUpdateOnGithub(author)
			if newData != None:
				if len(newData) > len(quotes):
					quotes = newData
					writeQuoteList(author,quotes)
			os.system("touch /tmp/{}.txt".format(author))
	print("Picking a random choice out of: {}".format(quotes))
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