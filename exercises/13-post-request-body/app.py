import requests


datos_json = {
    "id":2323,
    "title": "Very big project"
        }

resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php", json=datos_json)

print(resp.text)

print(resp.status_code)