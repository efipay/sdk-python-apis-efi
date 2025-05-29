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
        'expiracao': 600
    },
    'devedor': {
        'nome': '',
        'cpf': ''
    },
    'valor': {
        'original': ''
    },
    'chave': '',
    'solicitacaoPagador': None,
    'infoAdicionais': [
        {
            'nome': 'Nome 01',
            'valor': 'valor 01'
        }
    ]
}

response =  efi.pix_update_charge(params=params,body=body)
print(response)

