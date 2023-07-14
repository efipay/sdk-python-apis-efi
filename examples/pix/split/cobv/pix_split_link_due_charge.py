# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'txid': '',
    'splitConfigId': ''
}

response =  efi.pix_split_link_due_charge(params=params)
print(response)

