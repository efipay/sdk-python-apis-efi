# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'e2eId': '',
    'id': 0
}

body = {
    'valor': ''
}

response =  efi.pix_devolution(params=params,body=body)
print(response)

