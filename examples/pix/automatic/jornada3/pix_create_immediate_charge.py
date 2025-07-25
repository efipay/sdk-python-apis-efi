# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '',
        'nome': ''
    },
    'valor': {
        'original': ''
    },
    'chave': '',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  efi.pix_create_immediate_charge(body=body)
print(response)
