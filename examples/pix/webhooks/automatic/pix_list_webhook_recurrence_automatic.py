# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

response =  efi.pix_list_webhook_recurrence_automatic()
print(response)
