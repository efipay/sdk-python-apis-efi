# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "identificadorAdesao": "urn:efi:49315a93-d39c-4564-9yyb-9a73678dbdb1",
    "endToEndId": "E00038166201907261559y6j6"
}

response = efi.of_list_automatic_pix_payment(params=params)
print(response)