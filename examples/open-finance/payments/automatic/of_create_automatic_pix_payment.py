# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "identificadorAdesao": "urn:efi:19ba4105-9ae2-4637-89f2-96506d3c8770",
  "pagamento": {
    "valor": "9.99",
    "data": "",
    "codigoCidadeIBGE": "5300108",
    "infoPagador": "Parcela 2x20"
  }
}

response = efi.of_create_automatic_pix_payment(body=body)
print(response)