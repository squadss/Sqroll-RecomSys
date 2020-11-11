from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "Fdi8u79pIEXGvMzZUglxtMRmc"
consumer_secret = "yvxKZLusE5GZUS2tJ6ZFdfQ9K1ZfN6Ie8tfKfDn2mFrEcPxRlQ"
access_token = "1313558487905910784-vCnDIrbDsfG6JkkBD7lANxv1ucpbu4"
access_token_secret = "FAUAcXS6CdUKSQ1woyQzO1OcSAUlXNMt2NkBlsFdqCAJK"


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(follow = ["24742040"])
