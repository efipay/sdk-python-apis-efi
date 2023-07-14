# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'txid': ''
}

body = {
  'devedor': {
    'logradouro': 'Alameda Souza, Numero 80, Bairro Braz',
    'cidade': 'Recife',
    'uf': 'PE',
    'cep': '70011750',
    'cpf': '12345678909',
    'nome': 'Francisco da Silva'
  },
  'valor': {
    'original': '123.45'
  },
  'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response = efi.pix_update_due_charge(params=params, body=body)
print(response)