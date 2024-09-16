# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

response = efi.pix_detail_due_charge_batch(params=params)
print(response)