import requests

def get_attachment_by_id(attachment_id):
    adjuntos = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    datos_json = response.json()
    
    for i in datos_json["posts"]:
        if i["id"] == attachment_id:
           adjuntos.append(i["atachments"])
    return adjuntos

print(get_attachment_by_id(137))