# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'name': 'My Plan',
    'limit': 1,
    'offset': 0
}

response =  efi.list_plans(params=params)
print(response)
