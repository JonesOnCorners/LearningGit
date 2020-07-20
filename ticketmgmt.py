class Ticket:
    __counter = 0
    
    def __init__(self, passenger_name, source, destination):
        self.ticket_id = None
        self.passenger_name = passenger_name
        self.source = source
        self.destination = destination
    
    def validate_source_destination(self):
        if self.source == 'Delhi' and self.destination in ('Mumbai', 'Chennai', 'Pune', 'Kolkata'):
            return True
        return False
        
    
    def generate_ticket(self):
        if self.validate_source_destination():
            self.ticket_id = self.source[0] + self.destination[0] + Ticket.increment_counter()
            return self.ticket_id
        self.ticket_id = None
        return self.ticket_id
    
    @staticmethod
    def increment_counter():
        self.__counter += 1



t1 = Ticket('Jaydeep','Delhi','Mumbai')            
print(t1.generate_ticket())
