# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

headers = {
    'x-idempotency-key': 'et sedaute sint officiapariatur amet tute sum'
}

body = {
  "identificador": "urn:efi:19ba4105-9ae2-4637-89f2-96506d3c8770",
  "nomeFavorecido": "Marco Antonio de Brito",
  "status": "revogado",
  "dataExpiracao": "2021-05-21",
  "valorMaximo": "4.22"
}

response = efi.of_update_automatic_enrollment(body=body, headers=headers)
print(response)