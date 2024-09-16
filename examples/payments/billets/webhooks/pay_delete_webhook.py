# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "url": ""
}

response = efi.pay_list_webhook(body=body)
print(response)