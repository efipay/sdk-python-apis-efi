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
    "idParticipante": "75db457a-612d-4d62-b557-ba9d32b05216",
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
    "valor": "9.99",
    "codigoCidadeIBGE": "3540000",
    "infoPagador": "Churrasco",
    "idProprio": "6236574863254",
    "dataAgendamento": "2024-08-06"
  }
}

response = efi.of_start_schedule_pix_payment(body=body)
print(response)
