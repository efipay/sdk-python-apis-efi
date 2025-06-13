# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'txid': ''
}

body = {
  'calendario': {
    'dataDeVencimento': '2023-12-01',
    'validadeAposVencimento': 30
  },
  'devedor': {
    'logradouro': 'Alameda Souza, Numero 80, Bairro Braz',
    'cidade': 'Recife',
    'uf': 'PE',
    'cep': '70011750',
    'cpf': '12345678909',
    'nome': 'Francisco da Silva'
  },
  'valor': {
    'original': '123.45',
    'multa': {
      'modalidade': 2,
      'valorPerc': '15.00'
    },
    'juros': {
      'modalidade': 2,
      'valorPerc': '2.00'
    },
    'desconto': {
      'modalidade': 1,
      'descontoDataFixa': [
        {
          'data': '2022-11-30',
          'valorPerc': '30.00'
        }
      ]
    }
  },
  'chave': '',
  'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response = efi.pix_create_due_charge(params=params, body=body)
print(response)