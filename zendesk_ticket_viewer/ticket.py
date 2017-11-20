import abc

# Interface to be used for tickets
class Ticket(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self,data ):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

#
class ZendeskTicket(Ticket):

    def __init__(self,data):
        self.id = data['ticket']['id']
        self.subject = data['ticket']['subject']
        self.description = data['ticket']['description']
        self.updated_at = data['ticket']['updated_at']

    def __str__(self):
        return'\n {} \n {} \n {} \n {}' .format(self.id, self.subject,self.description,self.updated_at)


