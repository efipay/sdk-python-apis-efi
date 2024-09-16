# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'e2eId': '',
    'id': 0
}

response =  efi.pix_detail_devolution(params=params)
print(response)

