import requests
import json

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)

json = json.loads(response.text)
segundo_elemento = json[1]
nombre_proyecto = segundo_elemento["name"]

print(nombre_proyecto)