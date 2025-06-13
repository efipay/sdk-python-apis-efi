# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "identificadorAdesao": "urn:efi:19ba4105-9ae2-4637-89f2-96506d3c8770",
  "endToEndId": "E000000000000000000000000"
}

response = efi.of_cancel_automatic_pix_payment(body=body)
print(response)