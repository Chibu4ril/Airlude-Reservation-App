
class TicketConfig:
    def __init__(self, customer_id, fullname, ticket_number, seat_number, booking_time, status, ticket_type, window_seat):
        self.customer_id = customer_id
        self.fullname = fullname
        self.ticket_number = ticket_number
        self.seat_number = seat_number
        self.booking_time = booking_time
        self.status = status
        self.ticket_type = ticket_type
        self.window_seat = window_seat

    def prep_payload(self):
        payload = {  'customer_id' : self.customer_id , 'fullname': self.fullname, 'ticket_number' : self.ticket_number, 'seat_number':self.seat_number, 'booking_time':self.booking_time, 'status': self.status, 'ticket_type': self.ticket_type, 'window_seat' :self.window_seat }
        return payload

    @classmethod
    def payload_unwrapper(cls, data):
        new_payload = cls(
            customer_id = data['customer_id'],
            fullname = data['fullname'],
            ticket_number = data['ticket_number'],
            seat_number = data['seat_number'],
            booking_time = data['booking_time'],
            status = data['status'],
            ticket_type = data['ticket_type'],
            window_seat =  data['window_seat']
        )
        return new_payload

    @classmethod
    def customer_id(cls):
        c_id_range = range(0, 3)
        count = 0
        customerId = []
        while count <= 3:
            for i in c_id_range:
                random_range = random.randrange(5)
                customerId.append(i + random_range)
            break
        random_num_gen = ''.join(str(item) for item in customerId )
        return random_num_gen

    @classmethod
    def booking_id(cls):
        c_id_range = range(0, 5)
        bookingId = []
        booking_digit_count = 0
        while booking_digit_count <= 5:
            for i in c_id_range:
                random_range = random.randrange(5)
                bookingId.append(i + random_range)
            break
        random_booking_gen = ''.join(str(item) for item in bookingId)
        return random_booking_gen

