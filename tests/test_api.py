import pytest
from zendesk_ticket_viewer.api import ZendeskApi
from tests.fixtures.mock_zdesk import MockZdesk
from tests.fixtures.mock_os import MockOs
from tests.fixtures import example_output_all_tickets

@pytest.fixture
def Zdesk():
    Zdesk = MockZdesk
    return Zdesk

@pytest.fixture
def os():
    os = MockOs('1234asdf', 'test@sample.com', 'www.test.com')
    return os

@pytest.mark.unitTest
def test_connect_succeed(os, Zdesk):
        assert ZendeskApi.attempt_connection(os, Zdesk) == True


@pytest.mark.unitTest
def test_connect_fail_incorrect_password(os, Zdesk):
        os.token = '1234asd'
        assert ZendeskApi.attempt_connection(os, Zdesk) == False

@pytest.mark.unitTest
def test_connect_fail_incorrect_email(os, Zdesk):
        os.email = 'wrong@email.com'
        assert ZendeskApi.attempt_connection(os, Zdesk) == False

@pytest.mark.unitTest
def test_connect_fail_incorrect_subdomain(os, Zdesk):
        os.subdomain = 'www.wrongaddress.com.au'
        assert ZendeskApi.attempt_connection(os, Zdesk) == False

@pytest.mark.unitTest
def test_connect_fail_no_internet_connect(os, Zdesk):
        os.subdomain = 'NO_INTERNET_CONNECTION'
        assert ZendeskApi.attempt_connection(os, Zdesk) == False


@pytest.mark.unitTest
def test_setCredentials_success(os):
    ZendeskApi.set_credentials(os)
    assert ZendeskApi.access_token == '1234asdf'
    assert ZendeskApi.zendesk_email_address == 'test@sample.com'
    assert ZendeskApi.zendesk_subdomain == 'www.test.com'


@pytest.mark.unitTest
def test_setCredentials_incorrect_system_var_names(os):
    #TODO Currently not sure how I can create a test for this
    NotImplemented


@pytest.mark.unitTest
def test_all_tickets(os, Zdesk):
    ZendeskApi.attempt_connection(os, Zdesk)
    assert ZendeskApi.all_tickets() == example_output_all_tickets.data()

@pytest.mark.unitTest
def test_asingle_ticket(os, Zdesk):
    id = 1
    ZendeskApi.attempt_connection(os, Zdesk)
    assert ZendeskApi.single_ticket(id)

#TODO Implement tests for bad HTTP responses #

#TODO Implement test for single_ticket
#  Not currently sure how to best go about doing this.
