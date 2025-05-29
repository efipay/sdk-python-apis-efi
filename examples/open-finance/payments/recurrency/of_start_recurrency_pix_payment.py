# encoding: utf-8

import os
import sys
from efipay import EfiPay

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

from credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
  "pagador": {
    "idParticipante": "e69c25b5-c63a-4c25-8564-81f57436481c",
    "cpf": "45204392050",
    "cnpj": "90293071000112"
  },
  "favorecido": {
    "contaBanco": {
      "nome": "Lucas Silva",
      "documento": "17558266300",
      "codigoBanco": "09089356",
      "agencia": "0001",
      "conta": "654984",
      "tipoConta": "CACC"
    }
  },
  "pagamento": {
    "valor": "9.90",
    "codigoCidadeIBGE": "3540000",
    "infoPagador": "Churrasco",
    "idProprio": "6236574863254",
    "recorrencia": {
      "tipo": "diaria",
      "dataInicio": "2025-12-31",
      "quantidade": 2,
      "diaDaSemana": "SEGUNDA_FEIRA",
      "diaDoMes": 15,
      "datas": [
        "2024-08-01",
        "2024-08-08",
        "2024-08-15"
      ],
      "descricao": "Petshop"
    }
  }
}

response = efi.of_start_recurrency_pix_payment(body=body)
print(response)