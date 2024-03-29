from tweepy_test import search_tweet
import random
tweets = {}
tweetsPerCat = 20


def multiSearch(categories):
    for key in categories:
        tweets[key] = search_tweet(key)


def pullTweets(numPull=3):
    results = []
    for values in tweets.values():
        randoms = random.sample(values, numPull)
        results.extend(randoms)
    for i in random.sample(results, len(results)):
        print(i.text)
        print("\n")
    return random.sample(results, len(results))

"""
def main():
    multiSearch(["sports", "entertainment"])
    for i in pullTweets(3):
        print(i.text)
        print("\n")
        print("\n")



if __name__ == "__main__":
    main()
"""
