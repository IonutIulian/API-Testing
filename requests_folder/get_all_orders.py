import requests

def get_all_orders(token):
    headers_params = {'Authorization': token}
    response = requests.get("https://simple-books-api.glitch.me/orders",headers= headers_params)
    return response