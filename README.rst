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

**Parameters:**

Parameter | Type | Required | Description
------------ | ------------ |------------- | -------------
recipient_list | List | Yes | List of all the recipients. The expected format is 'Name `<email>`' or '`<email>`'.
subject | String | Yes* | The subject of the email. *In case your sending an email with template and pass `use_template_subject` as `True` then you don't need to pass the `subject`.
message | String | Yes* | The `message` of the email. *Just pass this if your gonna send a simple text email.
tags | Dict/List | No | The `tags` must be an dictionary containing keys and simple values or an list with strings.
from_name | String | No* | The name of the sender. *In case your sending an email with template and pass `use_template_from` as `True` then you don't need to pass the `from_name`.
from_email | String | Yes* | The email of the sender. *In case your sending an email with template and pass `use_template_email` as `True` then you don't need to pass the `from_email`.
template_name | String | Yes* | The `template_name` is the slug of the template. *Just pass this if your gonna send a email with template.
use_template_from | Bool | No* | If set to `True` it use the default value set to the sender's name.
use_template_email | Bool | No* | If set to `True` it use the default value set to the sender's email.
use_template_subject | Bool | No* | If set to `True` it use the default value set to the subject.
context | Dict | No | Global variables use in the Template. The format is expressed in the example (above).
context_per_recipient | Dict | No | Variables set for each recipient. The format is expressed in the example (above).
