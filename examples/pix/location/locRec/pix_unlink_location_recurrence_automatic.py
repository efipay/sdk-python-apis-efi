# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

response =  efi.pix_unlink_location_recurrence_automatic(params=params)
print(response)

