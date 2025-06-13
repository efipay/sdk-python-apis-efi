# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

headers = {
    'x-skip-mtls-checking': 'true'
}

body = {
  "webhookUrl": "https://usuario.recebedor.com/api/webhookrec/"
}

response =  efi.pix_config_webhook_recurrence_automatic(body=body, headers=headers)
print(response)
