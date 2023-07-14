# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)


params = {
    'id': 1
}

body = {
    'description': 'This charge was not fully paid'
}

response =  efi.create_charge_history(params=params, body=body)
print(response)
