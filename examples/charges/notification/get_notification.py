# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'token': ''
}

response =  efi.get_notification(params=params)
print(response)
