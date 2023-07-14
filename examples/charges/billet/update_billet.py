# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'expire_at': '2023-12-12'
}

response =  efi.update_billet(params=params, body=body)
print(response)
