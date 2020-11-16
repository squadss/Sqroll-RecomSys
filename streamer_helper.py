from queue import PriorityQueue

newCat = None


class SearchCategory():

    def __init__(self):
        self.tweets = PriorityQueue()

    def getTweets(self):
        return self.tweets


def newObject():
    newCat = SearchCategory()
    return newCat


def getter():
    return newCat