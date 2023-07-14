# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'idPagamento': 1
}

response = efi.pay_detail_payment(params=params)
print(response)