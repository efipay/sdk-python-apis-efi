# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "txid": "fc9a4366jf3d4964b5dba6c91a8722d3" 
}

response = efi.pix_detail_automatic_charge(params=params)
print(response)