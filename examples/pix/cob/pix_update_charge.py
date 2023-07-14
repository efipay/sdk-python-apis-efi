# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

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

