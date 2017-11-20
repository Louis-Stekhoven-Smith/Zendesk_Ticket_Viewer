import pytest
import io
import sys
from zendesk_ticket_viewer import ticket
from tests.fixtures import example_zendeskTicket

@pytest.fixture()
def zendesk_ticket():
     testTicket = ticket.ZendeskTicket(example_zendeskTicket.data())
     return testTicket

@pytest.mark.unitTest
def test_zendesk_ticket_init():
    assert(zendesk_ticket().id == 1)
    assert (zendesk_ticket().subject == 'Sample ticket: Meet the ticket')
    assert (zendesk_ticket().description == 'Hi this is a test ticket\n')
    assert (zendesk_ticket().updated_at == '2017-11-18T07:20:59Z')

@pytest.mark.unitTest
def test_zendesk_ticket_str():
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    print(zendesk_ticket())  # Call function.
    sys.stdout = sys.__stdout__  # Reset redirect.

    assert '1' in capturedOutput.getvalue()
    assert 'Sample ticket: Meet the ticket' in capturedOutput.getvalue()
    assert 'Hi this is a test ticket\n' in capturedOutput.getvalue()
    assert '2017-11-18T07:20:59Z' in capturedOutput.getvalue()# Now works as before.
