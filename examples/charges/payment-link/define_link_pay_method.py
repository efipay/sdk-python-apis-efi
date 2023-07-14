# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)


params = {
    'id': ''
}

body = {
    'billet_discount': 1,
    'card_discount': 1,
    'message': '',
    'expire_at': '2023-12-12',
    'request_delivery_address': False,
    'payment_method': 'all' #'banking_billet', 'credit_card', 'all'
}

response = efi.define_link_pay_method(params=params, body=body)
print(response)
