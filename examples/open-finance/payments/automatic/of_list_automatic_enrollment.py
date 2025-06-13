# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2024-06-01T00:00:00Z',
    'fim': '2024-09-14T23:59:59Z',
    'status': '',
    'documento': ''
    # 'identificadorAdesao': '',
    # 'idProprio': '',
    # 'documento': ''
}

response = efi.of_list_automatic_enrollment(params=params)
print(response)