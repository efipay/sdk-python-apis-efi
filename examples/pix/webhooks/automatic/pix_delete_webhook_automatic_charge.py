# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

response =  efi.pix_delete_webhook_automatic_charge()
print(response)
