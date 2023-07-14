# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'billet_discount': 0,
    'card_discount': 0,
    'message': '',
    'expire_at': '2018-12-12',
    'request_delivery_address': False,
    'payment_method': 'all' #'banking_billet', 'credit_card', 'all'
}

response = efi.update_charge_link(params=params, body=body)
print(response)
