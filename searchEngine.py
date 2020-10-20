from topic_stream import get_tweet
import random
tweets = {}
numPerCat = 1
keywords = ["basketball", "anime"]


def multiSearch(keywords):
    print("STARTED multi")
    for word in keywords:
        tweets[word] = []
        generator = get_tweet(word)
        print("finished generator")
        for _ in range(numPerCat):
            print("tweet")
            tweets[word].append(next(generator)) 
    print("success")


def pullTweets(numTweets):
    results = []
    randoms = random.sample(range(1, numPerCat), numTweets)
    for word in tweets:
        values = tweets[word]
        for i in randoms:
            results.append(values[i])
    print(results)
    return results

def main():
    multiSearch(keywords)
    pullTweets(1)

if __name__ == "__main__":
    main()
