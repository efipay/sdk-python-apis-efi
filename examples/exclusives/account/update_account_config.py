# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'pix': {
        'receberSemChave': True,
        'chaves': {
            'insira-aqui-sua-chave': {
                'recebimento': {
                    'txidObrigatorio': False,
                    'qrCodeEstatico': {
                        'recusarTodos': False
                    }
                }
            }
        }
    }
}
response =  efi.update_account_config(body=body)
print(response)

