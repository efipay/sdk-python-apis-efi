# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
   "idSolicRec": ""
}

body = {
  "status": "CANCELADA"
}

response = efi.pix_update_request_recurrence_automatic(params=params, body=body)
print(response)