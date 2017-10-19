import json

variables = {
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
    "key": '1e4be7cdd03545958e34',
    "secret": 'cf8cdba282104ed88f0a'
}
server_uri_test = 'http://0.0.0.0:8000'

variables_mail_search = {'app_ids': '1001',
                         'start': '2017-02-27',
                         'end': '2017-09-26'}

variables_mail_search_ids = ['21da05e09a214bf',
                             '7b9332128a3f461',
                             '09f7ceac90fe4b3',
                             '0f39a611031c4ff',
                             'f2412b7062814de']


