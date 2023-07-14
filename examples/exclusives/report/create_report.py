# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'dataMovimento': '2022-04-24',
    'tipoRegistros': {
        'pixRecebido': True,
        'pixDevolucaoEnviada': False,
        'tarifaPixRecebido': True,
        'pixEnviadoChave': True,
        'pixEnviadoDadosBancarios': False,
        'pixDevolucaoRecebida': True
    }
}

response = efi.create_report(body=body)
print(response)