# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)


params = {
    'idEnvio': 1
}

body = {
    'valor': '0.01',
    'pagador': {
        'chave': ''
    },
    'favorecido': {
        'chave': ''
    }
}

response =  efi.pix_send(params=params, body=body)
print(response)

