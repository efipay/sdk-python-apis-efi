# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

response =  efi.pix_keys_bucket()
print(response)

