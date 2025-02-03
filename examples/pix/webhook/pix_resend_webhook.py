# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "tipo": "PIX_RECEBIDO", #PIX_RECEBIDO, PIX_ENVIADO, DEVOLUCAO_RECEBIDA, DEVOLUCAO_ENVIADA
  "e2eids": [
    "E09089356202412261300API229e5352",
    "E09089356202412261300API3149af57"
  ]
}

response =  efi.pix_resend_webhook(body=body)
print(response)
