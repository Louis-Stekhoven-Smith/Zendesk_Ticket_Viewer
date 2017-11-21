import abc
from zdesk.zdesk import AuthenticationError, ZendeskError, RateLimitError
from requests.exceptions import ConnectionError


# Environment variables used for authentication
ZENDESK_ACCESS_TOKEN = 'ZENDESK_ACCESS_TOKEN'
ZENDESK_EMAIL_ADDRESS = 'ZENDESK_EMAIL_ADDRESS'
ZENDESK_SUBDOMAIN = 'ZENDESK_SUBDOMAIN'


# Interface to be used for tickets
class Api(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def attempt_connection(self) -> bool:
        pass

    @abc.abstractmethod
    def all_tickets(self):
        pass

    @abc.abstractmethod
    def single_ticket(self):
        pass


# Handles establishing authentication with Zendesk and deals with making api requests
class ZendeskApi(Api):
    connection = None
    access_token = None
    zendesk_email_address = None
    zendesk_subdomain = None

    # Attempts to authenticate with Zendesk and then checks if the attempt was successful.
    @classmethod
    def attempt_connection(cls, os, Zendesk):
        if not ZendeskApi.set_credentials(os):
            print('\nSystem variables have not been set or have been incorrectly named.\n'
                  'System variable names should be: '
                  '{}\n {}\n {}\n' .format(ZENDESK_ACCESS_TOKEN, ZENDESK_EMAIL_ADDRESS, ZENDESK_SUBDOMAIN))
            return False

        # Attempt to authenticate
        ZendeskApi.connection = \
            Zendesk(cls.zendesk_subdomain, cls.zendesk_email_address, cls.access_token, True)

        # Test if the authentication/connection was successful
        if cls.make_request(cls.connection.tickets_list, None) is not False:
            return True
        return False

    # Returns all existing tickets from currently authenticated account
    @classmethod
    def all_tickets(cls):
        return cls.make_request(cls.connection.tickets_list, None)

    # Returns a single ticket found by id
    @classmethod
    def single_ticket(cls, id):
        return cls.make_request(cls.connection.ticket_show, id)

    # Helpers
    @classmethod
    def set_credentials(cls, os):
        cls.access_token = os.getenv(ZENDESK_ACCESS_TOKEN)
        cls.zendesk_email_address = os.getenv(ZENDESK_EMAIL_ADDRESS)
        cls.zendesk_subdomain = os.getenv(ZENDESK_SUBDOMAIN)

        # Checking required system variables exist and are set
        if (cls.access_token is None or cls.zendesk_email_address is None
           or cls.zendesk_subdomain is None):
            return False
        return True

    # Attempts to process an api request and handle any errors raised by the zendesk api wrapper
    @staticmethod
    def make_request(request, params):
        try:
            if(params is None):
                return request()
            return request(params)

        except AuthenticationError as e:
            print(e)
            print("\nFailed to connect - Incorrect authentication details.")
            return False

        except ZendeskError as e:

            print("\nBad HTTP response - See raw response for more information.")
            print("%s %s" % ('\nRaw response: ', e))
            return False

        except ConnectionError as e:
            print(e)
            print("\nFailed to connect - No internet connection.")
            return False

        except RateLimitError as e:
            print(e)
            print("\nFailed to connect - Rate limit Reached .")
            return False
