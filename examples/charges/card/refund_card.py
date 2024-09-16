# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
  "amount": 1000
}

response = efi.refund_card(params=params, body=body)
print(response)
