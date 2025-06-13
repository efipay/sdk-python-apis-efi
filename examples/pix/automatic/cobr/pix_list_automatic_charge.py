# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
   'inicio': '2025-06-12T16:01:35Z',
   'fim': '2025-12-23T16:01:35Z',
#    'idRec': '',
#    'cpf': '',
#    'cnpj': '',
#    'locationPresente': #True or False ,
#    'status': '',
#    'convenio': '',
}

response = efi.pix_list_automatic_charge(params=params)
print(response)