

# TicketConfig class handles the creation and manipulation of active ticket details.

class TicketConfig:
    def __init__(self, customer_id, fullname, ticket_number, seat_number, booking_time, status, window_seat):
        # Initialize the ticket props
        self.customer_id = customer_id
        self.fullname = fullname
        self.ticket_number = ticket_number
        self.seat_number = seat_number
        self.booking_time = booking_time
        self.status = status
        self.window_seat = window_seat

    # Prepares the ticket's props as a dictionary for easy access or storage
    def prep_payload(self):
        payload = { "customer_id" : self.customer_id , 'fullname': self.fullname, 'ticket_number' : self.ticket_number, 'seat_number':self.seat_number, 'booking_time':self.booking_time, 'status': self.status, 'window_seat' :self.window_seat }
        return payload

    @classmethod
    def payload_unwrapper(cls, data):
        # Converts a dictionary back into a TicketConfig object
        new_payload = cls(
            customer_id = data["customer_id"],
            fullname = data['fullname'],
            ticket_number = data['ticket_number'],
            seat_number = data['seat_number'],
            booking_time = data['booking_time'],
            status = data['status'],
            window_seat =  data['window_seat']
        )
        return new_payload



# CancelledTicketConfig handles the ticket details specifically for cancelled reservations.
class CancelledTicketConfig:
    def __init__(self, customer_id, fullname, ticket_number, seat_number, booking_time, status, window_seat, cancelled_date):
        self.customer_id = customer_id
        self.fullname = fullname
        self.ticket_number = ticket_number
        self.seat_number = seat_number
        self.booking_time = booking_time
        self.status = status
        self.window_seat = window_seat
        self.cancelled_date = cancelled_date

    def cancelled_ticket_payload(self):
        """Return the ticket as a dictionary for CSV writing."""
        payload = {
            "customer_id": self.customer_id,
            "fullname": self.fullname,
            "ticket_number": self.ticket_number,
            "seat_number": self.seat_number,
            "booking_time": self.booking_time,
            "status": self.status,
            "window_seat": self.window_seat,
            "cancelled_date": self.cancelled_date
        }
        return payload

    @classmethod
    def payload_unwrapper_2(cls, data):
        """Convert a dictionary back into a CancelledTicketConfig object."""
        cancelled_payload = cls(
            customer_id=data["customer_id"],
            fullname=data["fullname"],
            ticket_number=data["ticket_number"],
            seat_number=data["seat_number"],
            booking_time=data["booking_time"],
            status=data["status"],
            window_seat=data["window_seat"],
            cancelled_date=data["cancelled_date"]
        )
        return cancelled_payload





