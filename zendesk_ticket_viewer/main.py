from tests.fixtures import example_zendeskTicket
from zendesk_ticket_viewer.ticket import ZendeskTicket
from zendesk_ticket_viewer.api import ZendeskApi
from zdesk import Zendesk
import os


# quick dirty code to test current functionality
def main():

    if not ZendeskApi.attempt_connection(os, Zendesk):
        pass
    else:

        print(ZendeskApi.all_tickets())
        try:
            print(ZendeskTicket(ZendeskApi.single_ticket(1)['ticket']))
        except:
            print('error')
        for rawTicketData in ZendeskApi.all_tickets():
            try:
                print(ZendeskTicket(rawTicketData))
            except:
                break
    #print(newTicket)
    return True


#TODO implement single ticket

#TODO implement main menu

if __name__ == "__main__":
    main()


