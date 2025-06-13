# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "vinculo": {
    "contrato": "63100862",
    "devedor": {
      "cpf": "12345678909",
      "nome": "Francisco da Silva"
    },
    "objeto": "Serviço de Streamming de Música."
  },
  "calendario": {
    "dataFinal": "2026-04-01",
    "dataInicial": "2025-06-01",
    "periodicidade": "MENSAL"
  },
  "valor": {
    "valorRec": "35.00"
  },
  "politicaRetentativa": "NAO_PERMITE",
  "loc": 108,
  "ativacao": {
    "dadosJornada": {
      "txid": "33beb661beda44a8928fef47dbeb2dc5"
    }
  }
}

response = efi.pix_create_recurrence_automatic(body=body)
print(response)