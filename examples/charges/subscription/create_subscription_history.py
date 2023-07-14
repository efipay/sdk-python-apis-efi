# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'description': 'This subscription was not fully paid'
}

response =  efi.create_subscription_history(params=params, body=body)
print(response)
