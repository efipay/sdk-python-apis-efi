# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'codBarras': 1
}

body = {
    'valor': 9300,
    'dataPagamento': '2022-06-17',
    'descricao': 'Pagamento de boleto, teste API Pagamentos'
}

response = efi.pay_request_bar_code(params=params, body=body)
print(response)