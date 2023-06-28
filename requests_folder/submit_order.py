import requests

def submit_order(bookid, customername, token):
    headers_params = {'Authorization': token}
    request_body = {
        "bookid": f"{bookid}",
        "customername": f"{customername}"
    }
    response = requests.post("https://simple-books-api.glitch.me/orders/",json=request_body, headers=headers_params)
    return response