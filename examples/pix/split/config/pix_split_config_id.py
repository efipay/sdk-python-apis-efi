# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': ''
}

body = {
    'descricao': '',
    'lancamento': {
        'imediato': True
    },
    'split': {
        'divisaoTarifa': 'assumir_total',
        'minhaParte': {
            'tipo': 'porcentagem',
            'valor': '60.00'
        },
        'repasses': [
            {
                'tipo': 'porcentagem',
                'valor': '15.00',
                'favorecido': {
                    'cpf': '',
                    'conta': ''
                }
            },
            {
                'tipo': 'porcentagem',
                'valor': '25.00',
                'favorecido': {
                    'cpf': '',
                    'conta': ''
                }
            }
        ]
    }
}

response =  efi.pix_split_config_id(params=params, body=body)
print(response)

