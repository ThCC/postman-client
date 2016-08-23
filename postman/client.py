from django.conf import settings
from postman import endpoint, Api
from django.core.exceptions import ImproperlyConfigured


class PostMan(Api):

    def __init__(self, key=None, secret=None, debug=False, fail_silently=False):
        super(PostMan, self).__init__(fail_silently)

        if debug:
            self.server_uri = 'http://0.0.0.0:8001/'
        else:
            self.server_uri = 'http://postman.alterdata.com.br/'

        if not hasattr(settings, 'ALTERDATA_MAIL_KEY') and not key:
            raise ImproperlyConfigured('API Key must be present in django settings or set in the constructor')
        if not hasattr(settings, 'ALTERDATA_MAIL_SECRET') and not secret:
            raise ImproperlyConfigured('API Secret must be present in django settings or set in the constructor')

        self._api_key = settings.ALTERDATA_MAIL_KEY if not key else key
        self._api_secret = settings.ALTERDATA_MAIL_SECRET if not secret else secret

    @endpoint(Api.POST, '/api/send_mail/')
    def send(self, mail):
        response = self.request(payload=mail.payload)
        return response

    @endpoint(Api.POST, '/api/send_mail/template/')
    def send_template(self, mail):
        response = self.request(payload=mail.payload)
        return response
