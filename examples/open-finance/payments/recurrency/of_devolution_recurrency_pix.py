# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'identificadorPagamento': ''
}

body = [
  {
    "endToEndId": "",
    "valor": "0.01"
  }
]

response = efi.of_devolution_recurrency_pix(params=params, body=body)
print(response)
