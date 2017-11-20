from zendesk_ticket_viewer import ticket
from tests.fixtures import example_zendeskTicket
from zendesk_ticket_viewer.ticket import ZendeskTicket


def main():
    newTicket = ZendeskTicket(example_zendeskTicket.data())

    print(newTicket)
    return True


if __name__ == "__main__":
    main()


