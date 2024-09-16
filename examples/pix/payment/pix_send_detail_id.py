# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'idEnvio': ''
}

response =  efi.pix_send_detail_id(params=params)
print(response)

