import tweepy

consumer_key = "Fdi8u79pIEXGvMzZUglxtMRmc"
consumer_secret = "yvxKZLusE5GZUS2tJ6ZFdfQ9K1ZfN6Ie8tfKfDn2mFrEcPxRlQ"
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


#print(api.search(q = ["movie"], lang = "en", count = 1, result_type = "popular"))

#FIGURE OUT WHAT TYPE AND HOW TO MANIPULATE
#related tags


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.new_session()
myStream._run()
