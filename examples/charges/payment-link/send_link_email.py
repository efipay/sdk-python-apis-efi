# encoding: utf-8

from efipay import EfiPay
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 1
}

body = {
    'email': 'oldbuck@efipay.com.br'
}

response =  efi.send_link_email(params=params)
print(response)
