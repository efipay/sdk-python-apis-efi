# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'e2eId': ''
}

response =  efi.pix_detail_received(params=params)
print(response)

