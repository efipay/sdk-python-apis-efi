# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': ''
}

response =  efi.pix_split_detail_config(params=params)
print(response)

