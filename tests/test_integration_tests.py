import pytest
from zendesk_ticket_viewer.api import ZendeskApi
import zdesk
import os


@pytest.mark.intergrationTest
def test_connect_succeed():
    assert ZendeskApi.attempt_connection(os, zdesk.Zendesk) is True


@pytest.mark.intergrationTest
def test_connect_fail_incorrect_password():
    os.environ['ZENDESK_ACCESS_TOKEN'] = '123asd'
    assert ZendeskApi.attempt_connection(os, zdesk.Zendesk) is False


@pytest.mark.intergrationTest
def test_connect_fail_incorrect_email():
    os.environ['ZENDESK_EMAIL_ADDRESS'] = 'wrong@email.com'
    assert ZendeskApi.attempt_connection(os, zdesk.Zendesk) is False


@pytest.mark.intergrationTest
def test_connect_fail_incorrect_subdomain():
    os.environ['ZENDESK_SUBDOMAIN'] = 'https://www.wrongaddress.com.au'
    assert ZendeskApi.attempt_connection(os, zdesk.Zendesk) is False


@pytest.mark.intergrationTest
def test_set_credentials_success():
    os.environ['ZENDESK_ACCESS_TOKEN'] = '1234asdf'
    os.environ['ZENDESK_EMAIL_ADDRESS'] = 'test@sample.com'
    os.environ['ZENDESK_SUBDOMAIN'] ='www.test.com'

    ZendeskApi.set_credentials(os)

    assert ZendeskApi.access_token is '1234asdf'
    assert ZendeskApi.zendesk_email_address == 'test@sample.com'
    assert ZendeskApi.zendesk_subdomain == 'www.test.com'


# TODO Currently not sure how I can create a test for this
@pytest.mark.intergrationTest
def test_set_credentials_incorrect_system_var_names():
    return NotImplemented


# TODO Implement tests for bad HTTP responses #

# TODO Implement test for single_ticket
#  Not currently sure how to best go about doing this.
