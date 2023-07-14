# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'name': 'My first plan',
    'repeats': 24,
    'interval': 2
}

response =  efi.create_plan(body=body)
print(response)
