# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
   'idRec': ''
}

body = {
  "loc": 108,
  "vinculo": {
    "devedor": {
      "nome": "Fulano de Tal"
    }
  },
  "calendario": {
    "dataInicial": "2024-04-01"
  },
  "ativacao": {
    "dadosJornada": {
      "txid": "33beb661beda44a8928fef47dbeb2dc5"
    }
  }
}

response = efi.pix_update_recurrence_automatic(params=params, body=body)
print(response)