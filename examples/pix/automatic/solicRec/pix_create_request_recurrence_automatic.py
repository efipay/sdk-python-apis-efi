# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "idRec": "RN123456782024011577825445612",
  "calendario": {
    "dataExpiracaoSolicitacao": "2025-05-20T12:17:11.926Z"
  },
  "destinatario": {
    "agencia": "2569",
    "conta": "550689",
    "cpf": "12345678909",
    "ispbParticipante": "91193552"
  }
}

response = efi.pix_create_request_recurrence_automatic(body=body)
print(response)