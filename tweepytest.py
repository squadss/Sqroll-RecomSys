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

print(type(myStream.filter(track=['python'])))

#print(myStream.filter(follow=["2211149702"]))

print("\n\n\n\n YESSIR")

try:
    print("Start streaming.")
    myStream.sample(languages=["en"])
except KeyboardInterrupt:
    print("Stopped.")
finally:
    print("Done.")
    myStream.disconnect()
   
