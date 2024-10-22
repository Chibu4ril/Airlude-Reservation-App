class Tickets:
    def __init__(self):
        self.totalTicket = 100

    def booked_ticket(self, booking):
        self.totalTicket - booking

request = Tickets()

print(request.booked_ticket(50))

#
#
# if __init__ = '__main__':
#
