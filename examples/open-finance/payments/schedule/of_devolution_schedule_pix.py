# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
  'identificadorPagamento': 'urn:'
}

body = {
    'valor': '0.01'
}

response = efi.of_devolution_schedule_pix(params=params, body=body)
print(response)
