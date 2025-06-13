# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
   'idRec': ''
}

response = efi.pix_detail_recurrence_automatic(params=params)
print(response)