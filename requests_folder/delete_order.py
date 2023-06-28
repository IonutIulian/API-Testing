import requests

def delete_order(orderid,token):
    headers_params= {'Authorization':token}
    response = requests.delete(f"https://simple-books-api.glitch.me/orders/{orderid}",headers= headers_params)
    return response