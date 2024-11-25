import csv
from ticketconfig import TicketConfig
from ticketconfig import CancelledTicketConfig

TICKETS_FILE = 'flight_db.csv'
CANCELLED_TICKETS = "cancelled_tickets.csv"


class CSVQuery:
    def __init__(self):
        self.all_tickets = self.query_tickets()
        self.all_cancelled_tickets = self.query_cancelled_tickets()

    def query_tickets(self):
        """
        Reads ticket data from a CSV file and returns a list of ticket objects.
        If the file doesn't exist, it creates a new file with headers and returns an empty list.
        If the file exists, it converts each row into a ticket object using TicketConfig.payload_unwrapper(row).
        """
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
        """Write ticket data to the CSV file."""
        with open(TICKETS_FILE, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat']
            )
            writer.writeheader()
            for ticket in tickets:
                writer.writerow(ticket.prep_payload())
            record.flush()
        return

    def write_to_cancelled_csv(self, cancelled_tickets):
        """Write cancelled ticket data to the CSV file."""
        with open(CANCELLED_TICKETS, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat', 'cancelled_date'])
            writer.writeheader()
            for ticket in cancelled_tickets:
                writer.writerow(ticket.cancelled_ticket_payload())
            record.flush()
        return





