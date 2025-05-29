# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

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