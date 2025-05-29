# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-04-29',
    'fim': '2024-12-29'
}

response = efi.of_list_recurrency_pix_payment(params=params)
print(response)