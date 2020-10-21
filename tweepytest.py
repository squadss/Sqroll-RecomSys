import tweepy

consumer_key = "Fdi8u79pIEXGvMzZUglxtMRmc"
consumer_secret = "yvxKZLusE5GZUS2tJ6ZFdfQ9K1ZfN6Ie8tfKfDn2mFrEcPxRlQ"
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


print(api.search(q = ["basketball", "anime"], lang = "en", count = 1, result_type = "popular"))

#FIGURE OUT WHAT TYPE AND HOW TO MANIPULATE
#related tags


