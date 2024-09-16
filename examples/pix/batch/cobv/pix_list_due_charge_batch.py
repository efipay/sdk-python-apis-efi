# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "inicio": "2020-01-01T00:00:00Z",
    "fim": "2024-12-01T23:59:59Z",
}

response = efi.pix_list_due_charge_batch(params=params)
print(response)