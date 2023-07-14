# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials


efi = EfiPay(credentials.CREDENTIALS)

body = {
    'items': [{
        'name': 'Product 1',
        'value': 1100,
        'amount': 2
    }],
    'shippings': [{
        'name': 'Default Shipping Cost',
        'value': 100
    }]
}

response =  efi.create_charge(body=body)
print(response)
