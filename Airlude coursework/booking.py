import csv
from datetime import datetime

from ticketconfig import TicketConfig
import random


TICKETS_FILE = 'flight_db.csv'


class Ticketing:
    def __init__(self):
        self.all_tickets = self.query_tickets()
        self.config_ticket = TicketConfig

    def query_tickets(self):
        all_tickets = []
        try:
            with open(TICKETS_FILE, mode='r') as records:
                parse = csv.DictReader(records)
                all_tickets = [TicketConfig.payload_unwrapper(row) for row in parse]
        except FileNotFoundError:
            print('No record found!')
        return all_tickets

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
        random_num_gen = ''.join(str(item) for item in customerId)
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

    def book_seat(self):
        if len([ticket for ticket in self.all_tickets if ticket.status == 'active']) >= 100:
            print('All seats are booked!')
            return None
        ticket_number = f'{self.customer_id()} - {self.booking_id()}'
        customer_id = self.customer_id()
        seat_number = len([ticket for ticket in self.all_tickets if ticket.status == 'active']) + 1
        fullname = f'{input('Enter First Name: ').title()} {input('Enter Last Name: ').title()}'
        booking_time = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
        status = 'active'
        ticket_type = 'Economy'
        window_seat = [x for x in self.all_tickets if seat_number % 2 ==0]
        my_ticket = self.config_ticket(customer_id, fullname, ticket_number, seat_number, booking_time, status, ticket_type, window_seat)
        self.all_tickets.append(my_ticket)
        with open(TICKETS_FILE, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'ticket_type', 'window_seat'])
            writer.writeheader()
            for ticket in self.all_tickets:
                writer.writerow(my_ticket.prep_payload())
        print(f'{fullname} your ticket with the following details has been booked successfully!: \n{my_ticket.prep_payload()}')
        return my_ticket


