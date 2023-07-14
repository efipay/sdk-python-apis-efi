# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'notification_url': 'http://yourdomain.com',
    'custom_id': 'my_new_id'
}

response =  efi.update_carnet_metadata(params=params, body=body)
print(response)
