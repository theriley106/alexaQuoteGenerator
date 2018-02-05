import requests
import bs4
import re
allSkills = {}

def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def extractInfoFromPage(page):
	for i in page.select(".a-fixed-left-grid-inner"):
		print i.select(".s-access-title")[0].getText()
		print str(i).partition("uotes/dp/")[2].partition("/")[0]

def checkInReadme():
	return

def addAllSkillsFromPage(page):
	return

def getTotalSkillCount(url):
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	text = page.select("#s-result-count")[0].getText()
	extractInfoFromPage(page)
	return int(str(text).partition(" of ")[2].partition(" ")[0])

if __name__ == '__main__':
	url = 'https://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Atheriley106+quotes&page={0}'
	totalCount = getTotalSkillCount(url.format('1'))
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')


