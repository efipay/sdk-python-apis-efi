# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

# params = { #optional
#     'nome': 'Name of participant'
# }

response = efi.of_list_participants()
print(response)