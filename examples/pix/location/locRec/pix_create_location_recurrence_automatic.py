# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

response =  efi.pix_create_location_recurrence_automatic()
print(response)

