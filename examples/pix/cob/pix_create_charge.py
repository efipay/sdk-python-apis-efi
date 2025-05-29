# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from credentials import credentials

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
