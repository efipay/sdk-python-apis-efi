# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'codBarras': 1
}

response = efi.pay_detail_bar_code(params=params)
print(response)