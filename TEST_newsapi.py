from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')


x = newsapi.get_top_headlines(q = "trump", country = 'us', language = 'en', page_size = 50)
print(len(x["articles"]))


news = "abc-news, al-jazeera-english, associated-press, bleacher-report, bloomberg, business-insider, buzzfeed, cnn, cbs-news," \
        + "espn, fortune,fox-news,fox-sports,google-news, IGN, medical-news-today, national-geographic, nbc-news, politico, reuters," \
        + "techcrunch, the-verge, the-wall-street-journal, the-washington-post, time, vice-news, wired"

news1 = "espn, abc-news, associated-press, bloomberg, al-jazeera-english, business-insider, buzzfeed, IGN, politico"

news2 = "fox-sports, cnn, cbs-news, fortune, fox-news, google-news, nbc-news, medical-news-today, national-geographic"

news3 = "bleacher-report, reuters, techcrunch, the-verge, the-wall-street-journal, the-washington-post, time, vice-news, wired"

y = newsapi.get_everything(sources = news1, from_param = "2021-01-31", 
                            language = 'en', sort_by='relevancy', page_size = 100)
print(len(y["articles"]))

#print(y["articles"])

print(y["articles"][0])

print([i["source"] for i in y["articles"]])





"""
for i in x["articles"]:
    print(i)
    print("\n\n\n\n\n\n\n\n")

"""
"""
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

                                        

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()
"""