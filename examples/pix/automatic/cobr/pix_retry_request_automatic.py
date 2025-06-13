# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "txid": "",
    "data": ""
}

response = efi.pix_retry_request_automatic(params=params)
print(response)