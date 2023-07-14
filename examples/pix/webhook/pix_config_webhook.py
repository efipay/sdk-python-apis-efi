# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

headers = {
    'x-skip-mtls-checking': 'false'
}

params = {
    'chave': ''
}

body = {
    'webhookUrl': ''
}

response =  efi.pix_config_webhook(params=params, body=body, headers=headers)
print(response)
