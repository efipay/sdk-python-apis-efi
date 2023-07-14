# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1,
    'parcel': 1
}

body = {
    'expire_at': '2020-12-12'
}

response =  efi.update_carnet_parcel(params=params, body=body)
print(response)
