# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
  'identificadorPagamento': 'urn:teste'
}

response = efi.of_cancel_schedule_pix(params=params)
print(response)
