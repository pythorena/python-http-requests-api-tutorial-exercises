import requests
import json

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)

datos_json = response.json()

autor = datos_json["posts"][0]["author"]

print(autor)