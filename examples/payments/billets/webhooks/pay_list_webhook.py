# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "dataInicio": "2024-01-22T16:01:35Z",
    "dataFim": "2024-09-22T16:01:35Z"
}

response = efi.pay_list_webhook(params=params)
print(response)