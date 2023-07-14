# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'items': [{
        'name': 'Product 1',
        'value': 1000,
        'amount': 2,
        'marketplace': {
            'mode': 1,
            'repasses': [{
                'payee_code': 'Insira_aqui_o_indentificador_da_conta_destino',
                'percentage': 2500
            }]
          }
    }],
    'shippings': [{
        'name': 'Default Shipping Cost',
        'value': 100
    }],
    'payment': {
        'banking_billet': {
            'expire_at': '2021-12-12',
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