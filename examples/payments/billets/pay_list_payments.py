# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'dataInicio': '2020-10-22',
    'dataFim': '2022-06-23'
}

response = efi.pay_list_payments(params=params)
print(response)