# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

payment = {
    'payment': {
        'banking_billet': {
            'expire_at': '2022-12-12',
            'customer': {
                'name': 'Gorbadoc Oldbuck',
                'email': 'oldbuck@efipay.com.br',
                'cpf': '94271564656',
                'birth': '1977-01-15',
                'phone_number': '5144916523'
            }
        }
    }
}

response =  efi.define_subscription_pay_method(params=params, body=payment)
print(response)
