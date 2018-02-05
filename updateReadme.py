import requests
import bs4


def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def getTotalSkillCount(url):
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	text = page.select("#s-result-count")[0].getText()
	return int(str(text).partition(" of ")[2].partition(" ")[0])
if __name__ == '__main__':
	url = 'https://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Atheriley106+quotes&page={0}'
	print getTotalSkillCount(url.format('1'))
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')


