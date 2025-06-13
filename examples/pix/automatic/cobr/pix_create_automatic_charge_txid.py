# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "txid": "fc9a4366jf3d4964b5dba6c91a8722d3" 
}

body = {
  "idRec": "RR1234567820240115abcdefghijk",
  "infoAdicional": "Serviços de Streamming de Música e Filmes.",
  "calendario": {
    "dataDeVencimento": "2025-06-15"
  },
  "valor": {
    "original": "106.07"
  },
  "ajusteDiaUtil": True,
  "devedor": {
    "cep": "89256140",
    "cidade": "Uberlândia",
    "email": "abc.sebaastiao.tavares@mail.com",
    "logradouro": "Alameda Silva 1056",
    "uf": "MG"
  },
  "recebedor": {
    "agencia": "0001",
    "conta": "012345",
    "tipoConta": "CORRENTE"
  }
}

response = efi.pix_create_automatic_charge_txid(params=params, body=body)
print(response)