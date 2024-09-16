# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = { 
    "plan_id": 3,       
    "customer": {
        "email": "gorbadoc.oldbuck@gmail.com",
        "phone_number": "31123456789"
    },
    "items": [{
        "name": "Product 1",
        "value": 1000,
        "amount": 1
    }],
    "shippings": [{
        "name": "frete",
        "value": 1800
    }]
}

response =  efi.update_subscription(params=params, body=body)
print(response)
