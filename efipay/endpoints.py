# encoding: utf-8

from __future__ import unicode_literals
from six import iteritems
import json
import re
import requests
import base64
import os
from functools import partial

from .constants import Constants
from .exceptions import (
    MissingParametersError,
    UnauthorizedError,
    EndpointError,
    CertificateError
)
from .version import VERSION


class Endpoints(object):

    def __init__(self, options):
        super(Endpoints, self).__init__()
        self.token = None
        self.options = options
        self.endpoints = {}
        self.cert = False

        # seletor de ambiente (sandbox ou produção)
        self.urls = {
            'production': 'https://api.efipay.com.br/v1',
            'sandbox': 'https://api.efipay.com.br/v1'
        }
        use_sandbox = options.get('sandbox', False)
        self.base_url = self.urls['sandbox'] if use_sandbox else self.urls['production']

    def __getattr__(self, name):
        apis = Constants.APIS
        api_names = ['PIX', 'OPEN-FINANCE', 'PAYMENTS', 'OPENING-ACCOUNTS', 'STATEMENT']

        for api_name in api_names:
            if name in apis[api_name]['ENDPOINTS']:
                self.endpoints = apis[api_name]['ENDPOINTS']
                self.urls = apis[api_name]['URL']
                self.cert = True
                self.set_base_url()
                return partial(self.request, self.endpoints[name])

        if name in apis['CHARGES']['ENDPOINTS']:
            self.endpoints = apis['CHARGES']['ENDPOINTS']
            self.urls = apis['CHARGES']['URL']
            self.cert = False
            self.set_base_url()
            return partial(self.request, self.endpoints[name])

        raise AttributeError("'{0}' object has no attribute '{1}'".format(self.__class__.__name__, name))

    def set_base_url(self):
        use_sandbox = self.options.get('sandbox', False)
        self.base_url = self.urls['sandbox'] if use_sandbox else self.urls['production']

    def request(self, settings, **kwargs):
        if not self.base_url:
            raise EndpointError(404)

        oauth = self.authenticate()

        if oauth == 200:
            params = kwargs.get('params', {})
            body = kwargs.get('body', {})
            headers = kwargs.get('headers', {})

            response = self.send(settings, params, body, headers)

            try:
                return response.json()
            except Exception:
                if response is not None and response.text:
                    return {
                        'code': response.status_code,
                        'content': response.text
                    }
                return {'code': response.status_code}

        elif oauth == 404:
            raise CertificateError(404)
        else:
            raise UnauthorizedError(oauth)

    def send(self, settings, params, body, headers_complement):
        url = self.build_url(settings['route'], params)

        headers = {
            'Authorization': 'Bearer {0}'.format(self.token['access_token']),
            'api-sdk': 'efi-python-{0}'.format(VERSION),
            'Content-Type': 'application/json'
        }

        headers.update(headers_complement)

        if 'partner_token' in self.options:
            headers['partner-token'] = self.options['partner_token']

        if self.cert:
            cert = self.options.get('certificate')
            return requests.request(
                settings['method'],
                url,
                headers=headers,
                data=json.dumps(body),
                cert=cert
            )
        else:
            return requests.request(
                settings['method'],
                url,
                headers=headers,
                json=body
            )

    def authenticate(self):
        url = self.build_url(self.endpoints['authorize']['route'], {})

        if self.cert:
            auth_string = '{0}:{1}'.format(
                self.options['client_id'],
                self.options['client_secret']
            )
            auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
            payload = json.dumps({"grant_type": "client_credentials"})

            headers = {
                'Authorization': 'Basic {0}'.format(auth),
                'Content-Type': 'application/json'
            }

            if 'partner_token' in self.options:
                headers['partner-token'] = self.options['partner_token']

            cert = self.options.get('certificate')
            if cert and os.path.exists(cert):
                response = requests.post(url, headers=headers, data=payload, cert=cert)
            else:
                return 404
        else:
            headers = {
                'accept': 'application/json',
                'api-sdk': 'efi-python-{0}'.format(VERSION)
            }

            if 'partner_token' in self.options:
                headers['partner-token'] = self.options['partner_token']

            auth = (
                self.options['client_id'],
                self.options['client_secret']
            )
            auth_body = {'grant_type': 'client_credentials'}

            response = requests.post(
                url, headers=headers, auth=auth, json=auth_body
            )

        if response.status_code == 200:
            self.token = response.json()

        return response.status_code

    def build_url(self, route, params):
        params = params or {}
        route = self.remove_placeholders(route, params)
        return self.complete_url(route, params)

    def remove_placeholders(self, route, params):
        regex = r':(\w+)'
        matches = re.findall(regex, route)
        if matches:
            for attr in matches:
                if attr not in params:
                    raise MissingParametersError(attr)
                route = route.replace(':' + attr, str(params[attr]))
                del params[attr]
        return route

    def query_string(self, params):
        return '&'.join(
            '{0}={1}'.format(p, v) for p, v in iteritems(params)
        )

    def complete_url(self, route, params):
        qs = self.query_string(params)
        if qs:
            return '{0}{1}?{2}'.format(self.base_url, route, qs)
        return '{0}{1}'.format(self.base_url, route)
