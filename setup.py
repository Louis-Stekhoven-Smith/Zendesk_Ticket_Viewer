from setuptools import setup
import os

rootdir = os.path.abspath(os.path.dirname(__file__))

setup(
    name='zendesk_ticket_viewer',
    version=0.4,
    description='A command line tool to view Zendesk tickets',
    long_description= open(os.path.join(rootdir,'DESCRIPTION.rst')).read(),
    author='Louis Stekhoven-Smith',
    author_email='louis.stekhoven@gmail.com',
    packages=['zendesk_ticket_viewer'],
    install_requires=['requests','zdesk','pytest'],
    license='GPL-3.0',
    zip_safe=False
)
