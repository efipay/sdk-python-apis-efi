# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'items': [{
        'name': 'Product 1',
        'value': 1000,
        'amount': 2
    }],
    'shippings': [{
        'name': 'Default Shipping Cost',
        'value': 100
    }],
    'payment': {
        'credit_card': {
            'installments': 1,
            'payment_token': '5cffb658d047093b3fbdf7eff8c434c3d26a4bd1',
            'billing_address': {
                'street': 'Av. JK',
                'number': 909,
                'neighborhood': 'Bauxita',
                'zipcode': '35400000',
                'city': 'Ouro Preto',
                'state': 'MG'
            },
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

response = efi.create_one_step_charge(params=None, body=body)
print(response)
