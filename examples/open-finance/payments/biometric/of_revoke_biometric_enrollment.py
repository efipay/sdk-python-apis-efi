# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

headers = {
    'x-idempotency-key': 'et sedaute sint officiapariatur amet tute sum'
}

body = {
  "identificadorVinculo": "urn:efi:ae71713f-875b-4af3-9d85-0bcb43288847",
  "motivo": "Encerramento de contrato de vinculo"
}

response = efi.of_revoke_biometric_enrollment(body=body, headers=headers)
print(response)