import requests

endpoint = "http://127.0.0.1:8000/myapp/1/update/"

data = {

    "title":"Hello world my old friend",
    "author":"igbalode writter",



}

get_response = requests.put(endpoint,json=data)
