import praw
import pprint
import json

reddit = praw.Reddit(client_id='xUkB4kWNtVZrEA',
                    client_secret='b5giJobBOPdceFzt38XJ97o6TwjRpQ',
                    user_agent ='my user agent'
)

"""
reddit.subreddit("THREAD") returns an iterable of r/THREAD

'submission' is an object documented here: https://praw.readthedocs.io/en/latest/code_overview/models/submission.html

Currently, we are printing out the title and url of the top 10 hottest meme reddit photos.
We will figure out how to turn object into .json file later.
"""
for submission in reddit.subreddit('memes').hot(limit=10):
    print(submission.title)
    print(submission.url)
