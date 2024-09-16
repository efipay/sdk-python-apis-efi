# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-10-22',
    'fim': '2023-12-12'
}

response = efi.of_list_pix_payment(params=params)
print(response)