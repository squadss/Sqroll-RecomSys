from newsapi import NewsApiClient
from datetime import datetime
import sys

def first():

	newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')
	news1 = "espn, abc-news, associated-press, bloomberg, al-jazeera-english, business-insider, buzzfeed, IGN, politico"
	date = datetime.today().strftime('%Y-%m-%d')

	json = newsapi.get_everything(sources = news1, from_param = date, language = 'en', sort_by='relevancy', page_size = 100)

	return json

def second():

	newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')
	news2 = "fox-sports, cnn, cbs-news, fortune, fox-news, google-news, nbc-news, medical-news-today, national-geographic"
	date = datetime.today().strftime('%Y-%m-%d')

	json = newsapi.get_everything(sources = news2, from_param = self.date, language = 'en', sort_by='relevancy', page_size = 100)

	return json

def third():

	newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')
	news3 = "bleacher-report, reuters, techcrunch, the-verge, the-wall-street-journal, the-washington-post, time, vice-news, wired"
	date = datetime.today().strftime('%Y-%m-%d')

	json = newsapi.get_everything(sources = news3, from_param = date, language = 'en', sort_by='relevancy', page_size = 100)

	return json
	