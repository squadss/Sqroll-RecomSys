import tweepy
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


consumer_key = "Fdi8u79pIEXGvMzZUglxtMRmc"
consumer_secret = "yvxKZLusE5GZUS2tJ6ZFdfQ9K1ZfN6Ie8tfKfDn2mFrEcPxRlQ"
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

"""
for tweet in tweepy.Cursor(api.search, q='basketball').items(10):
    print(tweet.text)
    print("\n")
    print("\n")
    print("\n")
"""


print(api.search(q = "basketball", lang = "en", count = 1, result_type = "popular"))

#FIGURE OUT WHAT TYPE AND HOW TO MANIPULATE

