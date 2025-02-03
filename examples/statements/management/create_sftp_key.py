from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

response = efi.create_sftp_key()
print(response)