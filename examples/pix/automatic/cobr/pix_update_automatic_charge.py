# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "txid": "fc9a4366jf3d4964b5dba6c91a8722d3" 
}

body = {
    "status": "CANCELADA"
}

response = efi.pix_update_automatic_charge(params=params, body=body)
print(response)