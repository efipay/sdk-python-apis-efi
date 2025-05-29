# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-10-22',
    'fim': '2023-12-12'
}

response = efi.of_list_pix_payment(params=params)
print(response)