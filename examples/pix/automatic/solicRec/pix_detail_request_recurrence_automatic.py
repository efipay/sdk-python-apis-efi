# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
   "idSolicRec": ''
}

response = efi.pix_detail_request_recurrence_automatic(params=params)
print(response)