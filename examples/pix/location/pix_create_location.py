# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'tipoCob': 'cob'
}

response =  efi.pix_create_location(body=body)
print(response)

