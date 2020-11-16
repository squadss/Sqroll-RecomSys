import sys
import time
import random
from streamer import *


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
