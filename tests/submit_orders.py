from requests_folder.generate_token import generate_token
from requests_folder.get_orders import get_orders
from requests_folder.patch_order import patch_order
from requests_folder.submit_order import submit_order


class TestSubmitOrder:

    def test_submit_order(self):
        token = generate_token()
        response = submit_order(2,"Vio",token)
        assert response.status_code==201,"Error, wrong status code"
        assert response.json()["created"]==True,"Error"
        assert len(response.json()["orderid"])==21,"Error, orderid invalid"


        respons = patch_order(response.json()["orderid"],"Mihai",token)
        assert respons.status_code==204,"Error"


        responsa= get_orders(token)
        assert responsa.status_code==209,"Error"

