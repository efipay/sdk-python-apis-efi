# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
  "payment": {
    "credit_card": {
      "customer": {
        "name": "Gorbadoc Oldbuck",
        "cpf": "94271564656",
        "email": "email_do_cliente@servidor.com.br",
        "birth": "1990-08-29",
        "phone_number": "5144916523"
      },
      "billing_address": {
        "street": "Avenida Juscelino Kubitschek",
        "number": "909",
        "neighborhood": "Bauxita",
        "zipcode": "35400000",
        "city": "Ouro Preto",
        "complement": "",
        "state": "MG"
      },
      "payment_token": "5e8aee6844198f01926534faef91597de8d96c31"
    }
  }
}

response = efi.card_payment_retry(params=params, body=body)
print(response)
