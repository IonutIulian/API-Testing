import requests

def patch_order(orderid, customername,token):
    headers_params = {'Authorization': token}
    request_body = {
        "customername": f"{customername}"
    }
    response = requests.patch(f"https://simple-books-api.glitch.me/orders/{orderid}",json=request_body,headers=headers_params)
    return response