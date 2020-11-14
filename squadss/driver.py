import sys
import time
import random
from streamer import *
#from searchEngine import *      # or import whatever function you're using for pulling tweets



categories = []
queues = []
update_time = 5
num_tweets_per_category = 5

def queue():
    for category in categories:
        queues.append(streaming(category))

def update():
    printlst = []
    for queue in queues:
        if queue.qsize() < num_tweets_per_category:
            temp = queue.qsize()    # whatever size of queue is 
        else:
            temp = num_tweets_per_category
        for _ in range(temp):
            printlst.append(queue.get())  #thing from queue)
    printlst = random.sample(printlst, len(printlst))
    print(*printlst, sep="\n")
    return printlst


def main():
    categories = sys.argv[2:]
    queue()
    while True:
        print("-------------------------------------------------------------------------------------------------------------------------" + "\n")
        print("NEW UPDATE" + "\n")
        print("-------------------------------------------------------------------------------------------------------------------------")
        update()
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