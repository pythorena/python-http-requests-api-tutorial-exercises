import requests

def get_titles():
    # your code here
    titulos = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    datos_json = response.json() 

    for i in datos_json["posts"]:
        titulos.append(i["title"])
        
    return titulos


print(get_titles())