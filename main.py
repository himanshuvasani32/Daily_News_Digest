import requests
from send_email import send_email

api_key = "523011253c5341d898a5e25420a172ee"
url = "https://newsapi.org/v2/everything?" \
      "q=tesla&" \
      "sortBy=publishedAt&" \
      "apiKey=523011253c5341d898a5e25420a172ee&"\
      "language=en"

# To access the url
request = requests.get(url)

# To load the content to json file
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" + \
               article["url"] + 2*"\n"

body = body.encode("utf-8")

send_email(message=body)

