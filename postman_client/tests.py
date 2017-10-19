# coding=utf-8
try:
    from test_variables import variables, server_uri_test, variables_mail_search, variables_mail_search_ids
except ImportError:
    variables = False
import unittest
from models import Mail
from client import PostMan


class TestAuthentication(unittest.TestCase):
    def setUp(self):
        if variables:
            self.server_uri_test = server_uri_test
            self.variables = variables
            self.variables_mail_search = variables_mail_search
            self.variables_mail_search_ids = variables_mail_search_ids
        else:
            self.server_uri_test = None
            self.variables = {
                "recipients": [
                    "Foo Bar <foo.bar@gmail.com>",
                    "Fulano Aquino <fulano.aquino@gmail.com>",
                    "<ciclano.norego@gmail.com>"
                ],
                "context_per_recipient": {
                    "foo.bar@gmail.com": {"foo": True},
                    "fulano.arquino@gmail.com.br": {"bar": True}
                },
                "from_name": 'Beutrano',
                "from_email": 'beutrano@gmail.com',
                "template_slug": 'test-101',
                "message_text": "Using this message instead.",
                "message_html": "<em>Using this message <strong>instead</strong>.</em>",
                "key": '2e7be7ced03535958e35',
                "secret": 'ca3cdba202104fd88d01'
            }
            self.variables_mail_search = {'app_ids': '1001',
                                          'start': '2017-02-27',
                                          'end': '2017-09-26'}

            self.variables_mail_search_ids = ["07f6b39e7e474b4", "8508657f502f4d4", "1afd55c4e995461"]

        self.postman = PostMan(key=self.variables['key'], secret=self.variables['secret'],
                               server_uri=self.server_uri_test)

    def test_method_post_text(self):
        mail = Mail(
            recipient_list=self.variables['recipients'],
            message_text=self.variables["message_text"],
            # remove comment if you gonna tested
            # message_html=self.variables["message_html"],
            from_name=self.variables['from_name'],
            from_email=self.variables['from_email'],
            subject="Just a test - Sended From Client"
        )
        response = self.postman.send(mail)
        if response and 'emails_enviados' in response:
            self.assertGreater(len(response['emails_enviados']), 0)
        else:
            self.assertIsNotNone(response)

    def test_method_post_template(self):
        mail = Mail(
            headers={'X_CLIENT_ID': 1},
            recipient_list=self.variables['recipients'],
            from_name=self.variables['from_name'],
            from_email=self.variables['from_email'],
            template_slug=self.variables['template_slug'],
            context={'foobar': True},
            context_per_recipient=self.variables['context_per_recipient'],
            # remove comment if you gonna tested
            # message_text=self.variables["message_text"],
            # message_html=self.variables["message_html"],
            use_tpl_default_subject=True,
            use_tpl_default_email=True,
            use_tpl_default_name=True,
            activate_tracking=True,
            get_text_from_html=True
        )
        response = self.postman.send_template(mail)
        if response and 'emails_enviados' in response:
            self.assertGreater(len(response['emails_enviados']), 0)
        else:
            self.assertIsNotNone(response)

    def test_method_get_mail_search(self):
        response = self.postman.mail_search(self.variables_mail_search)
        if response and len(response) > 0:
            self.assertGreater(len(response), 0)
        else:
            self.assertIsNotNone(response)

    def test_method_get_mail_search_by_ids(self):
        response = self.postman.mail_search_by_ids(self.variables_mail_search_ids)
        if response and len(response) > 0:
            self.assertGreater(len(response), 0)
        else:
            self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
