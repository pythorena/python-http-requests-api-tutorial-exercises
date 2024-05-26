import requests

def get_post_tags(post_id):
    posts = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    datos_json = response.json()
    
    for i in datos_json["posts"]:
        if i["id"] == post_id:
           posts.append(i["tags"])
    
    return posts


print(get_post_tags(146))



    