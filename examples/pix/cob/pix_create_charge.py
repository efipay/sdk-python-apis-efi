# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'txid': ''
}

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '',
        'nome': ''
    },
    'valor': {
        'original': '0.50'
    },
    'chave': '',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  efi.pix_create_charge(params=params,body=body)
print(response)
