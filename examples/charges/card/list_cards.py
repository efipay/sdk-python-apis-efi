# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'charge_type': 'card',
    'begin_date': '2024-01-01',
    'end_date': '2024-09-01'
    # "customer_document": ""
    # "status": ""
    # "custom_id": ""
    # "value": 
    # "date_of": ""
    # "limit": 
    # "page": 
    # "offset": 
}

response =  efi.list_charges(params=params)
print(response)
