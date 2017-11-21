from zendesk_ticket_viewer.api import ZENDESK_SUBDOMAIN,ZENDESK_EMAIL_ADDRESS,ZENDESK_ACCESS_TOKEN
class mock_os:

    def __init__(self, token, email, subdomain):
        self.token = token
        self.email = email
        self.subdomain = subdomain

    def getenv(self, string):
        if string == ZENDESK_ACCESS_TOKEN:
            return self.token
        if string == ZENDESK_EMAIL_ADDRESS:
            return self.email
        if string == ZENDESK_SUBDOMAIN:
            return self.subdomain

        return None




