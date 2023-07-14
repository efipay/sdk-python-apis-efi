# encoding: utf-8

from efipay import EfiPay
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


body = {
    'items': [{
        'name': 'Product One',
        'value': 600,
        'amount': 1
    }],
    'settings': {
        'billet_discount': 1,
        'card_discount': 1,
        'message': '',
        'expire_at': '2023-12-12',
        'request_delivery_address': False,
        'payment_method': 'all'
    }
}

response =  efi.create_one_step_link(body=body)
print(response)
