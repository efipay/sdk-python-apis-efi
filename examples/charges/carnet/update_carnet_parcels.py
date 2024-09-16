# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
  "parcels": [
      {
          "parcel": 1,
          "expire_at": "2024-01-10"
      },
    {
          "parcel": 2,
          "expire_at": "2024-02-11"
      },
    {
          "parcel": 3,
          "expire_at": "2024-03-15"
      },
    {
          "parcel": 4,
          "expire_at": "2024-04-19"
      }
  ]
}

response = efi.update_carnet_parcels(params=params, body=body)
print(response)
