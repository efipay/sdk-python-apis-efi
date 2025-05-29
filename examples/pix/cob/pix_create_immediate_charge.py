# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '16947588774',
        'nome': 'Victor'
    },
    'valor': {
        'original': '100.20'
    },
    'chave': '3670469c-f928-4361-ad2d-eb6ec189cb8c',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  efi.pix_create_immediate_charge(body=body)
print(response)