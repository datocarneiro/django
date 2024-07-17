import requests

def posts():
    url = f"https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    retorno = response.json()
    return retorno

