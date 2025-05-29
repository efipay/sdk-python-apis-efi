# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'descricao': 'Waask',
    'lancamento': {
        'imediato': True
    },
    'split': {
        'divisaoTarifa': 'assumir_total',
        'minhaParte': {
            'tipo': 'porcentagem',
            'valor': '85.00'
        },
        'repasses': [
            {
                'tipo': 'porcentagem',
                'valor': '15.00',
                'favorecido': {
                    'cpf': '',
                    'conta': ''
                }
            }
        ]
    }
}

response =  efi.pix_split_config(body=body)
print(response)

