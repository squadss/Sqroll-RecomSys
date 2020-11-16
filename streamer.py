from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from queue import PriorityQueue
from base_search import travel_base_search
import json
import twitter_credentials
import io
import time


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, start_time, time_limit=10):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []


    def on_data(self, data):
        #data = filter(data)

        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
        while (time.time() - self.time) < self.limit:
            try:
                self.tweet_data.append(data)
                return True
            except Exception as e:
                print('failed ondata, ', str(e))
                time.sleep(5)
                pass
        print(self.tweet_data)
        data = json.loads(data)
        print(data.get("text"))
        saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        exit()
    

        """
        data = json.loads(data)
        print(data.get("text"))
        self.tweets.put(-data.get("retweet_count", 0) - data.get("favorite_count", 0), data)
        return True
        """

    def on_error(self, status):
        print(status)


"""
def filter(data):
"""

def streaming(category):
    listener = StdOutListener(category)
    auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)

    stream = Stream(auth, listener)

    stream.filter(track = ["biden"], languages = ['en'], is_async = True, filter_level = "medium")


if __name__ == '__main__':
    streaming(time.time())




