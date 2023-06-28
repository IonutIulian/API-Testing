import requests


def get_order(token,orderid):
    headers_params = {'Authorization': token}
    response = requests.get(f"https://simple-books-api.glitch.me/orders/{orderid}",headers=headers_params)
    return response

