# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "id": 12069,
  "location": "pix.example.com/qr/v2/rec/2353c790eefb11eaadc10242ac120002",
  "criacao": "2023-12-20T12:38:28.774Z"
}

response =  efi.pix_create_location_recurrence_automatic(body=body)
print(response)

