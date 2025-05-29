# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2020-10-22T16:01:35Z',
    'fim': '2022-12-23T16:01:35Z'
}

response =  efi.pix_list_charges(params=params)
print(response)

