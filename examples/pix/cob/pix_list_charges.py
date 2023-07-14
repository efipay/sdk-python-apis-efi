# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2020-10-22T16:01:35Z',
    'fim': '2022-12-23T16:01:35Z'
}

response =  efi.pix_list_charges(params=params)
print(response)

