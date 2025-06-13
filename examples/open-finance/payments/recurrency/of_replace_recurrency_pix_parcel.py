# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'identificadorPagamento': '',
    'endToEndId': ''
}

body = {
  "valor": "9.99"
}

response = efi.of_replace_recurrency_pix_parcel(params=params, body=body)
print(response)
