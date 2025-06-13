# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'inicio': '2024-06-01',
    'fim': '2024-09-14',
    # 'status': ''          #Enum: pendente, rejeitado, aceito, expirado, cancelado
    # 'identificador': ''   #Exemplo : urn:efi:49315a93-d39c-4564-9edb-9a73678dbdb1
}

response = efi.of_list_biometric_pix_payment(params=params)
print(response)