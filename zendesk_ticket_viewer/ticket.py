import abc

''' Module description
 Handles formatting the api data received from zendesk into a user friendly format
 Format's for display:
    date
    subject
    description
    updated_at
    
Throws away all other data
'''

BORDER = '==================================================='


# Interface to be used for tickets
class Ticket(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __str__(self):
        pass


# Basic class to store ticket data
class ZendeskTicket(Ticket):

    def __init__(self, data):
        try:
            self.id = data['id']
            self.subject = data['subject']
            self.description = data['description']
            self.updated_at = data['updated_at']

        except KeyError:
            print("\nError - Zendesk changed ticket api response format, "
                  "please notify developers by raising an issue @\n"
                  "https://github.com/LouisKnuckles/Zendesk_Ticket_Viewer/issues\n")
            raise ValueError

    # Format's how data in the class is printed
    def __str__(self):
        return'{}\n' \
              'Ticket #1 {}\n' \
              'Subject: {}\n' \
              'Description: {}\n' \
              'Updated at: {}\n' \
              '{}'\
              .format(BORDER, self.id, self.subject, self.description, self.updated_at, BORDER)
