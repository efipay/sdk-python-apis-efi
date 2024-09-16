# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-04-29',
    'fim': '2024-12-29'
}

response = efi.of_list_recurrency_pix_payment(params=params)
print(response)