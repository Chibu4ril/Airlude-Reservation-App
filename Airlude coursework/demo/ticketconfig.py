
class TicketConfig:
    def __init__(self, customer_id, fullname, ticket_number, seat_number, booking_time, status, window_seat):
        self.customer_id = customer_id
        self.fullname = fullname
        self.ticket_number = ticket_number
        self.seat_number = seat_number
        self.booking_time = booking_time
        self.status = status
        self.window_seat = window_seat

    def prep_payload(self):
        payload = { 'customer_id' : self.customer_id , 'fullname': self.fullname, 'ticket_number' : self.ticket_number, 'seat_number':self.seat_number, 'booking_time':self.booking_time, 'status': self.status, 'window_seat' :self.window_seat }
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
            window_seat =  data['window_seat']
        )
        return new_payload





