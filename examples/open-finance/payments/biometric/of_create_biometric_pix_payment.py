# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

headers = {
    'x-idempotency-key': 'et sedaute sint officiapariatur amet tute sum'
}

body = {
  "identificadorVinculo": "enrollmentId",
  "favorecido": {
    "contaBanco": {
      "nome": "GORBADOCK SILVA",
      "documento": "01234567890",
      "codigoBanco": "09089356",
      "agencia": "0001",
      "conta": "654984",
      "tipoConta": "TRAN"
    }
  },
  "pagamento": {
    "valor": "250.00"
  }
}

response = efi.of_create_biometric_pix_payment(body=body, headers=headers)
print(response)