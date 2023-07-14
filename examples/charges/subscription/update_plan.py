# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'name': 'My new plan'
}

response =  efi.update_plan(params=params, body=body)
print(response)
