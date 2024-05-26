import requests
import json

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url)

json = json.loads(response.text)

print(json["name"])