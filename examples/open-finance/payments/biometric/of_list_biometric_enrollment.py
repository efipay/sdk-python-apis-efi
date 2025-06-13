# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'cpf': '',
    # 'cnpj': ''
}

response = efi.of_list_biometric_enrollment(params=params)
print(response)