from zdesk.zdesk import AuthenticationError
from requests.exceptions import ConnectionError
import json


class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

class MockZdesk:
    def __init__(self, ZENDESK_SUBDOMAIN, ZENDESK_EMAIL_ADDRESS, ACCESS_TOKEN, is_token):
        self.ZENDESK_SUBDOMAIN = ZENDESK_SUBDOMAIN
        self.ZENDESK_EMAIL_ADDRESS = ZENDESK_EMAIL_ADDRESS
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.is_token = is_token

    def tickets_list(self):
        if not(self.ZENDESK_SUBDOMAIN == 'www.test.com' and self.ZENDESK_EMAIL_ADDRESS == 'test@sample.com' and
                       self.ACCESS_TOKEN == '1234asdf' and self.is_token == True):
            raise AuthenticationError('Failed','401','Incorrect login details')
        if self.ZENDESK_SUBDOMAIN == 'NO_INTERNET_CONNECTION':
            raise ConnectionError

        return {'tickets': 'this is a test'}

    def ticket_show(self, id):
        return {'ticket': 'this is a test'}

