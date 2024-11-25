import csv
from ticketconfig import TicketConfig
from ticketconfig import CancelledTicketConfig

TICKETS_FILE = 'flight_db.csv'
CANCELLED_TICKETS = "cancelled_tickets.csv"

#  class to handle reading and writing ticket and cancelled ticket data from/to CSV files.
class CSVQuery:
    def __init__(self):
        # Initialize the CSVQuery class.
        # Queries both active tickets and cancelled tickets from their respective CSV files and stores them as instance variables.
        self.all_tickets = self.query_tickets()
        self.all_cancelled_tickets = self.query_cancelled_tickets()

    def query_tickets(self):
        # Reads ticket data from the TICKETS_FILE (flight_db.csv).
        all_tickets = []
        try:
            with open(TICKETS_FILE, mode='r') as records:
                all_tickets = [TicketConfig.payload_unwrapper(row) for row in csv.DictReader(records)]
        except FileNotFoundError:
            with open(TICKETS_FILE, mode='w', newline='') as record:
                csv.DictWriter(record,
                               fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time',
                                           'status', 'window_seat']).writeheader()
            print('No record found!')
        return all_tickets

    def query_cancelled_tickets(self):
        # Reads cancelled ticket data from the CANCELLED_TICKETS file (cancelled_tickets.csv).
        all_cancelled_tickets = []
        try:
            with open(CANCELLED_TICKETS, mode='r') as records:
                all_cancelled_tickets = [CancelledTicketConfig.payload_unwrapper_2(row) for row in csv.DictReader(records)]
        except FileNotFoundError:
            with open(CANCELLED_TICKETS, mode='w', newline='') as record:
                csv.DictWriter(record, fieldnames=["customer_id", "fullname", "ticket_number", "seat_number", "booking_time", "status", "window_seat", "cancelled_date"]).writeheader()
            print('No record found!')
        return all_cancelled_tickets

    def write_to_csv(self, tickets):
        # Writes the list of active ticket data to the TICKETS_FILE.
        # - Converts each ticket object to a dictionary/JSON using `ticket.prep_payload()
        with open(TICKETS_FILE, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat']
            )
            writer.writeheader()
            for ticket in tickets:
                writer.writerow(ticket.prep_payload())
            record.flush()
        return

    def write_to_cancelled_csv(self, cancelled_tickets):
        # Writes the list of cancelled ticket data to the CANCELLED_TICKETS file.
        # - Converts each cancelled ticket object to a dictionary using `ticket.cancelled_ticket_payload()`.

        with open(CANCELLED_TICKETS, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat', 'cancelled_date'])
            writer.writeheader()
            for ticket in cancelled_tickets:
                writer.writerow(ticket.cancelled_ticket_payload())
            record.flush()
        return





