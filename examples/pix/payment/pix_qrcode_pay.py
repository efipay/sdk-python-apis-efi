# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'idEnvio': 1
}

body = {
  "pagador": {
    "chave": "a1f4102e-a446-4a57-bcce-6fa48899c1d1",
    "infoPagador": "Pagamento de QR Code via API Pix"
  },
  "pixCopiaECola": "00020101021226830014BR.GOV.BCB.PIX2561qrcodespix.sejaefi.com.br/v2 41e0badf811a4ce6ad8a80b306821fce5204000053000065802BR5905EFISA6008SAOPAULO60070503***61040000"
}

response =  efi.pix_qrcode_pay(params=params, body=body)
print(response)

