from setuptools import setup

setup(
    name='zendesk_ticket_viewer',
    version=0.3,
    description='A command line tool to view Zendesk tickets',
    long_description='Displayed on pyPi project page.',
    author='Louis Stekhoven-Smith',
    author_email='louis.stekhoven@gmail.com',
    packages=['zendesk_ticket_viewer'],
    install_requires=['requests','zdesk','pytest'],
    license='GPL-3.0',
    zip_safe=False
)
