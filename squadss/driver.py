import sys
import time
import random
from streamer import *
#from searchEngine import *      # or import whatever function you're using for pulling tweets



update_time = 5                 # time until next update
num_tweets_per_category = 5     # number of tweets pulled per category we have

def queue(categories):
    """
    Returns a list of PQs of tweets based on categories.

        Parameters:
                categories (list of strings): A list of category names from command line args

        Returns:
                queues (list of PQs): A list of PQs based on streaming function
    """
    queues = []

    for category in categories:             
        queues.append(streaming(category))

    return queues

def update(queues):
    """
    Returns a scrambled list of tweets from len(categories) PQs.

        Parameters:
                queues (list of PQs): A list of PQs based on streaming function

        Returns:
                printlst (list of tweet objects): A list of up to num_tweets_per_category * len(queues) tweets, randomly arranged 
    """
    printlst = []

    for queue in queues:
        if queue.qsize() < num_tweets_per_category:
            temp = queue.qsize()
        else:
            temp = num_tweets_per_category

        for _ in range(temp):
            printlst.append(queue.get())

    printlst = random.sample(printlst, len(printlst))
    print(*printlst, sep="\n")
    return printlst


def main():
     """
    Takes command line inputs and runs the program.

        Parameters:
                argv (list of strings): command line inputs

        Returns:
                None
    """
    categories = sys.argv[2:]
    queues = queue(categories)

    while True:                             
        print("-------------------------------------------------------------------------------------------------------------------------" + "\n")
        print("NEW UPDATE" + "\n")
        print("-------------------------------------------------------------------------------------------------------------------------")
        update(queues)
        time.sleep(update_time)

if __name__ == "__main__":
    main()







"""





total_time = 60*10          # time to run whole script, in seconds
re_multiSearch_time = 60*2  # time until you call multiSearch again, in seconds
re_pull_time = 5            # time until you pull tweets from multiSearch, in seconds




t_end_all = time.time() + total_time

def search():
    if time.time() > t_end_all:
        exit()
    print("multiSearch")
    #multiSearch(keywords)
    return pull()


def pull():
    t_end = time.time() + re_multiSearch_time
    while time.time() < t_end:
        #pullTweets(numTweets)
        print("pullTweets")
        time.sleep(re_pull_time)
    return search()

search()


"""