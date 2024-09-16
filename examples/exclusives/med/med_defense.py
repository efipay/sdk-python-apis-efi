# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'idInfracao': '00000000-0000-0000-0000-000000000000',
}

body = {
    'analise': 'aceito',
    'justificativa': 'Justificativa'
}

response =  efi.med_defense(params=params, body=body)
print(response)

