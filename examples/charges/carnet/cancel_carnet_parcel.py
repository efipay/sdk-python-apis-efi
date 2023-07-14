# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1,
    'parcel': 1
}

response = efi.cancel_carnet_parcel(params=params)
print(response)
