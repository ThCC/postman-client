from distutils.core import setup

setup(
    name='postman-client',
    packages=['postman-client'],  # this must be the same as the name above
    version='0.1',
    description='Client service, to send simple text emails or, using a template created at Postman, send more complex emails.',
    author='Thiago Cardoso de Castro',
    author_email='thiago.decastro2@gmail.com',
    url='https://github.com/peterldowns/mypackage',  # use the URL to the github repo
    download_url='https://github.com/peterldowns/mypackage/tarball/0.1',  # I'll explain this in a second
    keywords=['testing', 'logging', 'example'],  # arbitrary keywords
    classifiers=[],
)
