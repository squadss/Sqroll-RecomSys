
import tweepy
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
api = tweepy.API(auth)
#print(api.search(q = "*", lang = "en", count = 10, result_type = "popular")[0]._json["entities"]["urls"][0]["url"])
tweets = api.search(q = "basketball", lang = "en", count = 100, result_type = "mixed")


storage = []
for i in tweets:
    storage.append(i._json["text"])

print(len(storage))
print(storage[7])

#print(api.trends_place(id = 2459115))