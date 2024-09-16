# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'identificadorPagamento': ''
}

response = efi.of_cancel_recurrency_pix(params=params)
print(response)
