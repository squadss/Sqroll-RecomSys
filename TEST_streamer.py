from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from queue import Queue
from base_search import *
import json
import twitter_credentials
import threading
import random


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self):
        # TODO: add maxsize?
        self.tweets = Queue()

    def on_data(self, data):
        data = json.loads(data)
        #print(data.get("text"))
        #-data.get("retweet_count", 0) - data.get("favorite_count", 0)
        # TODO: FIX PRIORITY QUEUE , putting two items with priority 0 fucks shit up, cuz get retweecount don work

        self.tweets.put(data)
        return True

    def on_error(self, status):
        print(status)


"""
def filter(data):
"""

def streaming(category):
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)

    stream = Stream(auth, listener)

    t1 = threading.Thread(target = runFilter, args = (stream, category))
    t1.start()

    return listener


def runFilter(stream, category):
    stream.filter(follow = eval(category + "Users").values(), track = eval(category + "Keywords"), languages = ['en'], is_async = True, filter_level = None)


if __name__ == '__main__':
    thing1 = streaming("art")

    print(thing1.tweets.get())
    print("\n\n\n\n\n\n\n\n" + "AHHHHHHHHHHHHLASBENYAAAAAAA")
    print(thing1.tweets.get())




