# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    "inicio": "2020-01-01T00:00:00Z",
    "fim": "2024-12-01T23:59:59Z",
}

response = efi.pix_list_due_charge_batch(params=params)
print(response)