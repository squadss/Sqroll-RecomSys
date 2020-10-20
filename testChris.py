from topic_stream import get_tweet

def main():
    generator = get_tweet("basketball")
    print(next(generator))
    gen = get_tweet("anime")
    print(next(gen))

if __name__ == "__main__":
    main()