# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'txid': '',
}

response =  efi.pix_split_unlink_charge(params=params)
print(response)

