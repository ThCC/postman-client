# -*- coding: utf-8 -*-
import json
from postman_client import endpoint, Api
from postman_client.exceptions import ImproperlyConfigured


class PostMan(Api):

    def __init__(self, key=None, secret=None, fail_silently=False, server_uri=None):
        super(PostMan, self).__init__(fail_silently)

        if server_uri:
            self.server_uri = server_uri
        else:
            self.server_uri = 'http://postman.alterdata.com.br'

        if not key:
            raise ImproperlyConfigured('A chave pública da API tem que ser passada no construtor')
        if not secret:
            raise ImproperlyConfigured('A chave privada da API tem que ser passada no construtor')

        self._api_key = key
        self._api_secret = secret

    @endpoint(Api.POST, '/api/send_mail/')
    def send(self, mail):
        response = self.request(payload=mail.get_payload())
        return response

    @endpoint(Api.POST, '/api/send_mail/template/')
    def send_template(self, mail):
        response = self.request(payload=mail.get_payload(endpoint='template'))
        return response

    @endpoint(Api.GET, '/api/mail/search/')
    def mail_search(self, args):
        self.search_mail_payload(endpoint='mail_search', args=args)
        response = self.request(payload=args)
        return response

    @endpoint(Api.GET, '/api/mail/search/specifics/')
    def mail_search_by_ids(self, uuids):
        self.search_mail_payload(endpoint='mail_search_ids', args=uuids)
        response = self.request(payload={'uuids': json.dumps(uuids)})
        return response

    def search_mail_payload(self, endpoint='text', args=None):
        param = None
        if endpoint == 'mail_search':
            if not args.get('app_ids'):
                param = 'app_ids'
            elif not args.get('start'):
                param = 'start'
            elif not args.get('end'):
                param = 'end'
        if endpoint == 'mail_search_ids':
            if not args:
                param = 'uuids'
        if param:
            raise AssertionError("Parâmetro " + param + " não foi fornecido.")
