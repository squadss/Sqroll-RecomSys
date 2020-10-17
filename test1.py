import requests

url = "https://api.twitter.com/2/tweets/1275828087666679809?tweet.fields=attachments,author_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source,text,withheld"

payload = {}
headers = {"Authorization": "Bearer {}".format('AAAAAAAAAAAAAAAAAAAAAELaIgEAAAAAtXWZfgXOTcMMk1KPaCKYDSFhtTo%3D453K3zQxmE0OEnOO1rgS5Jr7Zy2KwOZyONfEH4Shgg00cdfDAl')}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
print("hi")
