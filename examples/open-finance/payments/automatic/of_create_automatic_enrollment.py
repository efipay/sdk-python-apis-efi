# encoding: utf-8

from efipay import EfiPay
from ....credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "pagador": {
    "cpf": "01234567890",
    "cnpj": "01234567890123",
    "nome": "Josué Real",
    "idParticipante": "64c189e5-9d4a-4319-aa5e-d02c36e1815d"
  },
  "favorecido": {
    "contaBanco": {
      "nome": "Lucas Silva",
      "documento": "12345678901",
      "codigoBanco": "09089356",
      "agencia": "0001",
      "conta": "654984",
      "tipoConta": "TRAN"
    }
  },
  "assinatura": {
    "expiracao": "2026-08-27",
    "configuracao": {
      "automatico": {
        "intervalo": "ANUAL",
        "dataInicio": "2025-06-06",
        "valorFixo": "500.00",
        "valorMinimo": "450.00",
        "valorMaximo": "750.00",
        "permiteRetentativa": "",
        "primeiroPagamento": {
          "data": "2024-06-08",
          "valor": "9.99",
          "infoPagador": "Parcela 1"
        }
      }
    },
    "descricao": "Mensalidades do curso XYZ",
    "idProprio": "6236574863254"
  }
}

response = efi.of_create_automatic_enrollment(body=body)
print(response)