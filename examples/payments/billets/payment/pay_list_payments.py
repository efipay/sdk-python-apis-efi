# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'dataInicio': '2020-10-22',
    'dataFim': '2022-06-23'
}

response = efi.pay_list_payments(params=params)
print(response)