from zendesk_ticket_viewer.ticket import ZendeskTicket
from zendesk_ticket_viewer.api import ZendeskApi
from zdesk import Zendesk
import os

''' Module description
 The entry point for the application drives core functionality:
 Display a single zendesk ticket
 Display all zendesk tickets 
'''

BORDER = '==================================================='
DISPLAY_SINGLE_TICKET = '1'
DISPLAY_ALL_TICKETS = '2'
EXIT = '9'
CONNECTION_ERROR_MSG = ''


def main():
    set_up()
    while True:
        main_menu()
        selection = input(': ')

        if selection is DISPLAY_SINGLE_TICKET:
            display_single_ticket()

        elif selection is DISPLAY_ALL_TICKETS:
            display_all_tickets()

        elif selection is EXIT:
            print('\nGood Bye - Have a nice day ^_^')
            break
        else:
            print('Invalid selection\n')


# Welcome user and attempts to authenticate connection with zendesk api
def set_up():
    print('Welcome to the Zendesk Ticket Viewer')
    print('...Establishing connection')
    ZendeskApi.attempt_connection(os, Zendesk)


# Handles getting a tickets raw data from the Zendesk api and then attempts to display it
def display_single_ticket():
    id_number = input('Enter ticket id number: ')
    raw_response = ZendeskApi.single_ticket(id_number)

    if raw_response is False:
        return False

    display(raw_response)


# Handles getting all tickets raw data from the Zendesk api and then attempts to display them
def display_all_tickets():
    all_tickets_raw_data = ZendeskApi.all_tickets()

    if all_tickets_raw_data is False:
        return False

    for rawTicketData in ZendeskApi.all_tickets():
        display(rawTicketData)


# Formats raw ticket data received from api, into a user friendly format
def display(raw_response):
    try:
        formatted_ticket = ZendeskTicket(raw_response)
        print(formatted_ticket)
        return True
    except ValueError:
        pass
        return False


def main_menu():
    print('{}\n{}\n\n{}\n{}\n{}\n\n{}\n{}' .format(BORDER,
                                                   'Main Menu',
                                                   'Please enter one of the following options:',
                                                   '1. Display a single ticket',
                                                   '2. Display all tickets',
                                                   '9. Quit out of program',
                                                   BORDER))


if __name__ == '__main__':
    main()
