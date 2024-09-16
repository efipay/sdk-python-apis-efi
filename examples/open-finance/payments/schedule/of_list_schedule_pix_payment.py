# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-05-01',
    'fim': '2024-05-01'
}

response = efi.of_list_schedule_pix_payment(params=params)
print(response)
