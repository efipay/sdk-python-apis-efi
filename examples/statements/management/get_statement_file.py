from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'nome_arquivo': 'nome_arquivo'
}

response = efi.get_statement_file(params=params)
print(response)