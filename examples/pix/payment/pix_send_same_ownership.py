# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'idEnvio': ''
}

body = {
  "valor": "12.34",
  "pagador": {
    "chave": "19974764017",
    "infoPagador": "Segue o pagamento da conta"
  },
  "favorecido": {
    "chave": "joão@meuemail.com"
  }
}

response =  efi.pix_send_same_ownership(params=params, body=body)
print(response)

