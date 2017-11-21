from setuptools import setup, find_packages

setup(
    name='zendesk_ticket_viewer',
    version=0.1,
    description='A command line tool to view Zendesk tickets',
    long_description='Displayed on pyPi project page.',
    author='Louis Stekhoven-Smith',
    author_email='louis.stekhoven@gmail.com',
    packages=find_packages(),
    install_requires=['requests','zdesk','pytest','setuptools'],
    license='GPL-3.0'
)
