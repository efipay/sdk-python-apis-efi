# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

response =  efi.pix_unlink_txid_location(params=params)
print(response)

