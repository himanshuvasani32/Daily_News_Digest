import requests

api_key = "523011253c5341d898a5e25420a172ee"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=523011253c5341d898a5e25420a172ee"

# To access the url
request = requests.get(url)

# To load the content to json file
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
