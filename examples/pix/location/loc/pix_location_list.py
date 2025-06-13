# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-03-22T00:00:00.000Z',
    'fim': '2023-03-31T00:00:00.000Z'
}

response =  efi.pix_location_list(params=params)
print(response)

