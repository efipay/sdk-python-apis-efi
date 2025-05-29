# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2022-05-01',
    'fim': '2024-05-01'
}

response = efi.of_list_schedule_pix_payment(params=params)
print(response)
