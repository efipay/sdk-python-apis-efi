# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
  "cobsv": [
    {
      "calendario": {
        "dataDeVencimento": "2025-01-10"
      },
      "txid": "fb2761260e554ad593c7226beb5cb650",
      "valor": {
        "original": "110.00"
      }
    },
    {
      "calendario": {
        "dataDeVencimento": "2020-01-10"
      },
      "txid": "7978c0c97ea847e78e8849634473c1f1",
      "valor": {
        "original": "110.00"
      }
    }
  ]
}

response = efi.pix_update_due_charge_batch(params=params, body=body)
print(response)