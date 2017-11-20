import abc


# Interface to be used for tickets
class Ticket(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __str__(self):
        pass


# Basic class to store ticket data
class ZendeskTicket(Ticket):

    def __init__(self, data):
        self.id = data['ticket']['id']
        self.subject = data['ticket']['subject']
        self.description = data['ticket']['description']
        self.updated_at = data['ticket']['updated_at']

    # Format's how data in the class is printed
    def __str__(self):
        return'\n---------------------------------------------\n' \
              'Ticket #1 {}\n' \
              'Subject: {}\n' \
              'Description: {}\n' \
              'Updated at: {}\n'\
              '-----------------------------------------------'\
            .format(self.id, self.subject, self.description, self.updated_at)
