# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2021-01-14T16:01:35Z',
    'fim': '2023-12-15T16:01:35Z'
}

response =  efi.pix_received_list(params=params)
print(response)

