from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'periodicidade': "diario",
    'envia_email': True,
    'comprimir_arquivos': True
}

response = efi.create_statement_recurrency(body=body)
print(response)