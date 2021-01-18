from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='a89be3df1f42495ea5af3172cb83be03')


x = newsapi.get_top_headlines(sources='bbc-news, the-verge, cnn, fox-news')
print(x)

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