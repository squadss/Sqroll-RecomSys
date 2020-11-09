import time
from searchEngine import *      # or import whatever function you're using for pulling tweets



#RIP abstraction :(((

categories = ["sports", "entertainment"] # list of keywords, idk what it's supposed to be now
tweets = {} # dictionary of tweets, idk what it's supposed to be now

"""
you can change these
"""
total_time = 60*10          # time to run whole script, in seconds
re_multiSearch_time = 60*2  # time until you call multiSearch again, in seconds
re_pull_time = 5            # time until you pull tweets from multiSearch, in seconds


t_end_all = time.time() + total_time

def search():
    if time.time() > t_end_all:
        exit()
    #print("multiSearch")
    multiSearch(categories)
    return pull()


def pull():
    t_end = time.time() + re_multiSearch_time
    while time.time() < t_end:
        pullTweets()
        #print("pullTweets")
        time.sleep(re_pull_time)
    return search()

search()
