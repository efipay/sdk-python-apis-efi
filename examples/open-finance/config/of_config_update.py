# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  'redirectURL': '',
  'webhookURL': ''
}

response = efi.of_config_update(body=body)
print(response)