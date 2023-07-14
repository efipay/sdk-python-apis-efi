# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'description': 'This carnet is about a service'
}

response =  efi.create_carnet_history(params=params, body=body)
print(response)
