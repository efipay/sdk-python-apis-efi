# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'e2eid': 'E0000000000000000000000000000',
    # 'txid': '0000000000000000000000000000000',
    # 'idEnvio': '0000000000000000000000000000000',
    # 'rtrId':'D0000000000000000000000000000'
}


response =  efi.pix_get_receipt(params=params)
print(response)

