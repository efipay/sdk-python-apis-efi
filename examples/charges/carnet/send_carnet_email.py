# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'email': 'oldbuck@efipay.com.br'
}

response =  efi.send_carnet_email(params=params, body=body)
print(response)
