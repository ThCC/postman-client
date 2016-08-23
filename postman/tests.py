import unittest
from models import Mail
from client import PostMan


class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.postman = PostMan(key='1e4be7cdd03545958e34', secret='cf8cdba282104ed88f0a', debug=True)

    def test_method_post_text(self):
        mail = Mail(
            recipient_list=[
                  "Thiago de Castro <thiago.decastro2@gmail.com>",
                  "Thiago C de Castro <THIAGO.CIRRUS@ALTERDATA.COM.BR>",
                  "<success@simulator.amazonses.com>",
                  "<bounce@simulator.amazonses.com>",
                  "<ooto@simulator.amazonses.com>",
                  "<complaint@simulator.amazonses.com>",
                  "<suppressionlist@simulator.amazonses.com>"
              ],
            message="Apenas um teste. Pode deletar se quiser.",
            from_name='Postman',
            from_email='postman@alterdata.com.br',
            subject="Just a test"
        )
        response = self.postman.send(mail)
        if response and 'emails_enviados' in response:
            self.assertGreater(len(response['emails_enviados']), 0)
        else:
            self.assertIsNotNone(response)

    def test_method_post_template(self):
        mail = Mail(
            recipient_list=[
                "Thiago de Castro <thiago.decastro2@gmail.com>",
                "Thiago C de Castro <THIAGO.CIRRUS@ALTERDATA.COM.BR>",
                "<success@simulator.amazonses.com>",
                "<bounce@simulator.amazonses.com>",
                "<ooto@simulator.amazonses.com>",
                "<complaint@simulator.amazonses.com>",
                "<suppressionlist@simulator.amazonses.com>"
            ],
            from_name='Postman',
            from_email='postman@alterdata.com.br',
            template_name="teste-01",
            context={'foobar': True},
            context_per_recipient={
                "thiago.decastro2@gmail.com": {"foo": True},
                "thiago.cirrus@alterdata.com.br": {"bar": True}
            },
            use_template_subject=True,
            use_template_email=False,
            use_template_from=False
        )
        response = self.postman.send_template(mail)
        if response and 'emails_enviados' in response:
            self.assertGreater(len(response['emails_enviados']), 0)
        else:
            self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
