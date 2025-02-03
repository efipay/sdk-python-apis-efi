from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'identificador': "diario" # "diario", "semanal", "mensal"
}

body = {
    'periodicidade': "diario",
    'status': "ativo",
    'envia_email': True,
    'comprimir_arquivos': True
}

response = efi.update_statement_recurrency(params=params, body=body)
print(response)