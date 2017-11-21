import pytest
from zendesk_ticket_viewer.api import ZendeskApi
from tests.fixtures.mock_zdesk import MockZdesk
from tests.fixtures.mock_os import mock_os


@pytest.fixture
def zdesk():
    zdesk_object = MockZdesk
    return zdesk_object


@pytest.fixture
def os():
    osObject = mock_os('1234asdf', 'test@sample.com', 'www.test.com')
    return osObject


@pytest.mark.unitTest
def test_connect_succeed(os, zdesk):
        assert ZendeskApi.attempt_connection(os, zdesk) is True


@pytest.mark.unitTest
def test_connect_fail_incorrect_password(os, zdesk):
        os.token = '1234asd'
        assert ZendeskApi.attempt_connection(os, zdesk) is False


@pytest.mark.unitTest
def test_connect_fail_incorrect_email(os, zdesk):
        os.email = 'wrong@email.com'
        assert ZendeskApi.attempt_connection(os, zdesk) is False


@pytest.mark.unitTest
def test_connect_fail_incorrect_subdomain(os, zdesk):
        os.subdomain = 'www.wrongaddress.com.au'
        assert ZendeskApi.attempt_connection(os, zdesk) is False


@pytest.mark.unitTest
def test_connect_fail_no_internet_connect(os, zdesk):
        os.subdomain = 'NO_INTERNET_CONNECTION'
        assert ZendeskApi.attempt_connection(os, zdesk) is False


@pytest.mark.unitTest
def test_set_credentials_success(os):
    ZendeskApi.set_credentials(os)
    assert ZendeskApi.access_token is '1234asdf'
    assert ZendeskApi.zendesk_email_address == 'test@sample.com'
    assert ZendeskApi.zendesk_subdomain == 'www.test.com'


# TODO Currently not sure how I can create a test for this
@pytest.mark.unitTest
def test_set_credentials_incorrect_system_var_names():
    return NotImplemented


@pytest.mark.unitTest
def test_all_tickets(os, zdesk):
    ZendeskApi.attempt_connection(os, zdesk)
    assert ZendeskApi.all_tickets() == 'this is a test'


@pytest.mark.unitTest
def test_asingle_ticket(os, zdesk):
    id_number = 1
    ZendeskApi.attempt_connection(os, zdesk)
    assert ZendeskApi.single_ticket(id_number)

# TODO Implement tests for bad HTTP responses #

# TODO Implement test for single_ticket
#  Not currently sure how to best go about doing this.
