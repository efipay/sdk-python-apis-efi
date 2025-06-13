# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'chave': ''
}

response =  efi.pix_detail_webhook(params=params)
print(response)
