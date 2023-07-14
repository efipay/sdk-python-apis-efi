# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'brand': 'visa',
    'total': 5000
}

response =  efi.get_installments(params=params)
print(response)
