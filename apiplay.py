import requests
import pprint

x = 'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=US&key=AIzaSyCpK7GHz5YhDKt-QwHaT8piijue9zwWBxg' 

payload = {'part': 'snippet,contentDetails,statistics', 'chart': "mostPopular", 'regionCode': "US", 'key': 'AIzaSyCpK7GHz5YhDKt-QwHaT8piijue9zwWBxg'}
r = requests.get('https://youtube.googleapis.com/youtube/v3/videos', params = payload)

#pprint.pprint(r.json()['posts'][0]['url_for_post'])
#print(dir(r))

pprint.pprint(r.json())
