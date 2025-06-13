# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

headers = {
    'x-idempotency-key': 'et sedaute sint officiapariatur amet tute sum'
}

body = {
    "pagador": {
        "cpf": "01234567890",
        "idParticipante": "9326f9b2-ae57-42c4-a0d9-acc4ba434696"
    }
}

response = efi.of_create_biometric_enrollment(body=body, headers=headers)
print(response)