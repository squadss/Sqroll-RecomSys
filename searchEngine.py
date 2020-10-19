from topic_stream import get_tweet
import random
tweets = {}
keywords = ["basketball", "anime"]


def multiSearch(keywords):
    for word in keywords:
        tweets[word] = get_tweet(word)


def pullTweets(numTweets):
    results = []
    multiSearch(keywords)
    randoms = random.sample(range(1, 20), numTweets)
    for word in tweets:
        values = tweets[word]
        for i in randoms:
            results.append(values[i])
    return results

def refresh(numTweets):
    results = []
    randoms = random.sample(range(1, 20), numTweets)
    for word in tweets:
        values = tweets[word]
        for i in randoms:
            results.append(values[i])
    return results
        
