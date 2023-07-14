# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'items': [{
        'name': 'Product 1',
        'value': 1000,
        'amount': 2
    }]
}

response =  efi.create_subscription(params=params, body=body)
print(response)
