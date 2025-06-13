# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials
import base64

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

response =  efi.pix_generate_qrcode(params=params)
print(response)

#Generate QRCode Image
if('imagemQrcode' in response):
    with open('qrCodeImage.png', 'wb') as fh:
        fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))