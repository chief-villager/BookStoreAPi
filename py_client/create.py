import requests

endpoint = "http://127.0.0.1:8000/myapp"

data = {
    'title':'ali and simbi',
    'author': 'sola ogunde',

}

get_response = requests.post(endpoint,json=data)