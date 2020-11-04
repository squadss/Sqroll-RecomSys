import requests
import os
import json

"""
Run this file with: python3 topic_stream.py
Description: Will ask you for topic, and output ONE tweet about that topic.

The function that does the same thing without asking for input is called
get_tweet(topic), and can be found at the bottom of this file.
"""


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


"""def set_rules(headers, delete, bearer_token):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "basketball has:images", "tag": "basketball"},
        {"value": "nba has:images -grumpy", "tag": "nba"},
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))"""

#Only look for tweets with images by default
def set_rules(headers, delete, bearer_token, topic, images=True, tag=None):
    if not tag:
        tag = topic
    if images:
        sample_rules = [
            {"value": topic + " has: images", "tag": tag}
        ]
    else:
        sample_rules = [
            {"value": topic, "tag": tag}
        ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))

def get_stream(headers, set, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
    )
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )

    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            yield json_response
            #print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    load_token()
    input_stream()

"""
This function asks user for an input, and streams ONE tweet about this topic.
"""
def input_stream():
    topic = input("Topic: ")
    bearer_token = os.environ.get("BEARER_TOKEN")
    headers = create_headers(bearer_token)
    rules = get_rules(headers, bearer_token)
    delete = delete_all_rules(headers, bearer_token, rules)
    set = set_rules(headers, delete, bearer_token, topic)
    get_stream(headers, set, bearer_token, numTweets=1)

"""
Recommend using this function for your parts.
@param topic, is the topic of the tweet
@returns a generator, returing a .json file everytime you call next.
"""
def get_tweet(topic):
    load_token()
    bearer_token = os.environ.get("BEARER_TOKEN")
    headers = create_headers(bearer_token)
    rules = get_rules(headers, bearer_token)
    delete = delete_all_rules(headers, bearer_token, rules)
    set = set_rules(headers, delete, bearer_token, topic)
    return get_stream(headers, set, bearer_token)


def load_token():
    os.environ["BEARER_TOKEN"] = "AAAAAAAAAAAAAAAAAAAAAELaIgEAAAAAtXWZfgXOTcMMk1KPaCKYDSFhtTo%3D453K3zQxmE0OEnOO1rgS5Jr7Zy2KwOZyONfEH4Shgg00cdfDAl"



if __name__ == "__main__":
    main()
