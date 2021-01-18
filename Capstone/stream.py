from searchEngine import * 
from basewords import *
import webbrowser
import sys

def openBrowser(category):
    multiSearch(category)
    results = []
    for values in tweets.values():
        randoms = random.sample(values, 2)
        results.extend(randoms)
    for i in random.sample(results, len(results)):
        webbrowser.open('http://twitter.com/ILOVEVCG/status/' + str(i.id), new=2)
    return random.sample(results, len(results))

def main():
    categories = sys.argv[1:]
    openBrowser(categories)


if __name__ == "__main__":
    main()