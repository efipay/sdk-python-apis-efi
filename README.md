# SDK Python para APIs Efí Pay

> A python library for integration of your backend with the payment services
provided by [EfiPay](https://sejaefi.com.br/).

## Installation

Install with Pip:

```bash
$ pip install efipay
```
## Tested with
```
python 3.11
```
## Basic usage

```python
# encoding: utf-8

from efipay import EfiPay

credentials = {
    'client_id': 'client_id',
    'client_secret': 'client_secret',
    'sandbox': True,
    'certificate': 'insira-o-caminho-completo-do-certificado'
}

efi = EfiPay(credentials)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '12345678909',
        'nome': 'Francisco da Silva'
    },
    'valor': {
        'original': '123.45'
    },
    'chave': '71cdf9ba-c695-4e3c-b010-abb521a3f1be',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  efi.pix_create_immediate_charge(body=body)
print(response)

```

## Examples

You can run the examples inside `examples` with
`$ python -m examples/pix/cob/pix_create_immediate_charge`:

```bash
$ python -m examples/pix/cob/pix_create_immediate_charge
```

Just remember to set the correct credentials inside `examples/credentials/credentials.py` before running.

## Tests

To run the tests, just run *pytest*:

```bash
$ py.test
```

## Additional documentation

The full documentation with all available endpoints is in https://dev.gerencianet.com.br/.

## Changelog

[CHANGELOG](CHANGELOG.md)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/efipay/sdk-python-apis-efi. This project is intended to be a safe, welcoming space for collaboration.

## License

The library is available as open source under the terms of the [MIT License](LICENSE).
