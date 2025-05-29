# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
  'identificadorPagamento': 'urn:'
}

body = {
    'valor': '0.01'
}

response = efi.of_devolution_schedule_pix(params=params, body=body)
print(response)
