# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "idRec": "RR1234567820240115abcdefghijk",
  "infoAdicional": "Serviços de Streamming de Música e Filmes.",
  "calendario": {
    "dataDeVencimento": "2025-05-15"
  },
  "valor": {
    "original": "106.07"
  },
  "ajusteDiaUtil": True,
  "devedor": {
    "cep": "89256140",
    "cidade": "Uberlândia",
    "email": "sebastiao.tavares@mail.com",
    "logradouro": "Alameda Franco 1056",
    "uf": "MG"
  },
  "recebedor": {
    "agencia": "9708",
    "conta": "012682",
    "tipoConta": "CORRENTE"
  }
}
response = efi.pix_create_automatic_charge(body=body)
print(response)