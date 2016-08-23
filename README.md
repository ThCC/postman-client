Client service, to send simple text emails or, using a template created at Postman, send more complex emails.

In order to use this library, you must create an account in Postman.
** **It is not currently possible to create an account in Postman, but will soon be** **

Follow the examples below to send simple emails or emails with templates:

**Simple Emails:**

from postman.models import Mail
from postman.client import PostMan

class SendSimpleMail(object):
    postman = PostMan(key='<your_account_public_key>', secret='<your_account_secret_key>')

    def send(self):
        mail = Mail(
            recipient_list=[
                'Foo Bar <foo.bar@gmail.com>',
                'Fulano Aquino <fulano.aquino@gmail.com>',
                '<ciclano.norego@gmail.com>'
            ],
            message="Just a Test, delete if you want.",
            from_name='Beutrano',
            from_email='beutrano@gmail.com',
            subject="Just a test"
        )
        response = self.postman.send(mail)

**Template Emails:**

from postman.models import Mail
from postman.client import PostMan

class SendTemplateMail(object):
    postman = PostMan(key='<your_account_public_key>', secret='<your_account_secret_key>')

    def send(self):
        mail = Mail(
            recipient_list=[
                'Foo Bar <foo.bar@gmail.com>',
                'Fulano Aquino <fulano.aquino@gmail.com>',
                '<ciclano.norego@gmail.com>'
            ],
            from_name='Beutrano',
            from_email='beutrano@gmail.com',
            template_name='test-101',
            context={'foobar': True},
            context_per_recipient={
                "foo.bar@gmail.com": {"foo": True},
                "fulano.arquino@gmail.com.br": {"bar": True}
            },
            use_template_subject=True,
            use_template_email=False,
            use_template_from=False
        )
        response = self.postman.send_template(mail)

**Parameters and meaning:**

