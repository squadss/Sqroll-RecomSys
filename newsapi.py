from newsapi import NewsApiClient
from datetime import datetime
import sys

'''
These are 3 functions that return json files with 100 news articles. These functions should be called every 45 minutes, 15 minutes apart.
news_api_first() should be called, then 15 minutes later news_api_second() should be called and after 15 more minutes news_api_third() should be called.
15 minutes later, the cycle should repeat forever. In pseudocode:
while():
	news_api_first()
	15 minutes
	second()
	news_api_15 minutes
	news_api_third()
	15 minutes
'''

def news_api_first():

	newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')
	news1 = "espn, abc-news, associated-press, bloomberg, al-jazeera-english, business-insider, buzzfeed, IGN, politico"
	date = datetime.today().strftime('%Y-%m-%d')

	json = newsapi.get_everything(sources = news1, from_param = date, language = 'en', sort_by='relevancy', page_size = 100)

	return json

def news_api_second():

	newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')
	news2 = "fox-sports, cnn, cbs-news, fortune, fox-news, google-news, nbc-news, medical-news-today, national-geographic"
	date = datetime.today().strftime('%Y-%m-%d')

	json = newsapi.get_everything(sources = news2, from_param = self.date, language = 'en', sort_by='relevancy', page_size = 100)

	return json

def news_api_third():

	newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')
	news3 = "bleacher-report, reuters, techcrunch, the-verge, the-wall-street-journal, the-washington-post, time, vice-news, wired"
	date = datetime.today().strftime('%Y-%m-%d')

	json = newsapi.get_everything(sources = news3, from_param = date, language = 'en', sort_by='relevancy', page_size = 100)

	return json
	