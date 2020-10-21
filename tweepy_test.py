
import tweepy

consumer_key = "Fdi8u79pIEXGvMzZUglxtMRmc"
consumer_secret = "yvxKZLusE5GZUS2tJ6ZFdfQ9K1ZfN6Ie8tfKfDn2mFrEcPxRlQ"
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

keywords = {"sports": ["basketball", "soccer", "football", "espn", "baseball"],
            "entertainment": ["movies", "tv", "netflix", "celebrity", "disney", "marvel"],
}

#print(api.search(q = "basketball", lang = "en", count = 1, result_type = "popular"))

"""
For given category, returns list of associated keywords
@param category: the category we are searching for
@return <list> of keywords associated with category.
"""
def getKeywords(category):
    if category in keywords:
        return keywords[category]
    else:
        print("No data for category")


"""
@param category: the category of the tweets we are pulling
@returns Tweepy object found from search
"""
def search_tweet(category, num_tweets=20):
    keywords = getKeywords(category)
    searches = []
    tweets_per_keyword = num_tweets // len(keywords)
    for key in keywords:
        searches.extend(api.search(q = "basketball", lang = "en", count = tweets_per_keyword, result_type = "popular"))
    return searches


def main():
    print(search_tweet("sports"))


if __name__ == "__main__":
    main()
