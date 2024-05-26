import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)

json = json.loads(response.text)

print(json)

print("Hora actual: {} h {} min y {} seg".format(json['hours'], json['minutes'], json['seconds']))