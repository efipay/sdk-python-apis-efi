# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
	'inicio': '2022-01-22T00:00:00Z',
	'fim':'2024-12-31T23:59:59Z',
	# 'status': "REALIZADO", // "EM_PROCESSAMENTO", "REALIZADO", "NAO_REALIZADO"
	# 'devolucaoPresente': True,
	# 'paginacao.paginaAtual': 1,
	# 'paginacao.itensPorPagina': 10
}

response =  efi.pix_send_list(params=params)
print(response)

