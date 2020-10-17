curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Content-type: application/json" \
-H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAELaIgEAAAAAtXWZfgXOTcMMk1KPaCKYDSFhtTo%3D453K3zQxmE0OEnOO1rgS5Jr7Zy2KwOZyONfEH4Shgg00cdfDAl" -d \
'{
  "add": [
    {"value": "from:twitterdev from:twitterapi has:links"}
  ]
}'