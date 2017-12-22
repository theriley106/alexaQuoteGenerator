import os
import requests
import json

def checkForUpdateOnGithub(quoteAuthor):
	try:
		quoteAuthor = quoteAuthor.replace(' ', '_')
		url = "https://raw.githubusercontent.com/theriley106/alexaQuoteGenerator/master/QuoteDB/{}.txt".format(quoteAuthor)
		res = requests.get(url)
		print("Checking github for new quote for {}".format(quoteAuthor))
		if res.status_code == 404:
			print("Github returned 404 for {}".format(url))
			return None
		else:
			print("Github status was 200")
			listOfQuotes = list(set(str(res.text).split('\n')))
			if len(listOfQuotes) < 3:
				print("List of quotes on Github was < 3")
				return None
			else:
				print("Grabbed new quotes from Github")
				return listOfQuotes
	except:
		return None

def updateAppInfo():
	res = requests.get('https://raw.githubusercontent.com/theriley106/alexaQuoteGenerator/master/appInfo.json')
	data = res.json()
	with open('/tmp/appInfo.json', 'w') as f:
		json.dump(data, f)
	return json.load(open('/tmp/appInfo.json'))
	
def readAppInfo():
	if os.path.exists('/tmp/appInfo.json') == False:
		return updateAppInfo()
	else:
		return json.load(open('/tmp/appInfo.json'))