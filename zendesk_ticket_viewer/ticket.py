import abc


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
            print("Error - Zendesk changed ticket format, notify developer")
            raise ValueError

    # Format's how data in the class is printed
    def __str__(self):
        return'\n---------------------------------------------\n' \
              'Ticket #1 {}\n' \
              'Subject: {}\n' \
              'Description: {}\n' \
              'Updated at: {}\n'\
              '-----------------------------------------------'\
            .format(self.id, self.subject, self.description, self.updated_at)
