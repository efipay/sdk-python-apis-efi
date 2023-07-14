# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-10-22T16:01:35Z',
    'fim': '2023-10-23T16:01:35Z'
}

response =  efi.pix_list_webhook(params=params)
print(response)
