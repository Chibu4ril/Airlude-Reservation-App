import csv
from datetime import datetime
from ticketconfig import TicketConfig
from ticketconfig import CancelledTicketConfig
import random

TICKETS_FILE = 'flight_db.csv'
CANCELLED_TICKETS = "cancelled_tickets.csv"

class Ticketing:
    def __init__(self):
        self.all_tickets = self.query_tickets()
        # self.all_cancelled_tickets = self.query_cancelled_tickets()
        self.config_ticket = TicketConfig
        self.cancelled_ticket_config = CancelledTicketConfig
        self.counter = len([ticket for ticket in self.all_tickets if ticket.status == 'Active'])
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.all_cancelled_tickets = []



    def query_tickets(self):
        all_tickets = []
        try:
            with open(TICKETS_FILE, mode='r') as records:
                parse = csv.DictReader(records)
                all_tickets = [TicketConfig.payload_unwrapper(row) for row in parse]
        except FileNotFoundError:
            with open(TICKETS_FILE, mode='w', newline='') as record:
                writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat'])
                writer.writeheader()
            print('No record found!')
        return all_tickets

    def query_cancelled_tickets(self):
        all_cancelled_tickets = []
        try:
            with open(CANCELLED_TICKETS, mode='r') as records:
                parse = csv.DictReader(records)
                all_cancelled_tickets = [CancelledTicketConfig.payload_unwrapper_2(row) for row in parse]
        except FileNotFoundError:
            with open(CANCELLED_TICKETS, mode='w', newline='') as record:
                writer = csv.DictWriter(record, fieldnames=["customer_id", "fullname", "ticket_number", "seat_number", "booking_time", "status", "window_seat", "cancelled_date"])
                writer.writeheader()
            print('No record found!')
        return all_cancelled_tickets

    def assign_seat_number(self):
        while True:
            # Calculate the next seat number
            next_seat_number = len([ticket for ticket in self.all_tickets if ticket.status == 'Active']) + 1
            # Check if the seat number already exists
            if any(ticket.seat_number == str(next_seat_number) for ticket in self.all_tickets):
                print(f"Seat Number {next_seat_number} already exists. Trying the next seat number...")
            else:
                print(f"Assigned Seat Number: {next_seat_number}")
                return next_seat_number

    @classmethod
    def customer_id(cls):
        count = 0
        customerId = []
        while count <= 3:
            for i in  range(0, 3):
                random_range = random.randrange(5)
                customerId.append(i + random_range)
            break
        random_num_gen = ''.join(str(item) for item in customerId)
        return random_num_gen

    @classmethod
    def booking_id(cls):
        bookingId = []
        booking_digit_count = 0
        while booking_digit_count <= 5:
            for i in range(0, 5):
                random_range = random.randrange(5)
                bookingId.append(i + random_range)
            break
        random_booking_gen = ''.join(str(item) for item in bookingId)
        return random_booking_gen

    def write_to_csv(self):
        with open(TICKETS_FILE, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat'])
            writer.writeheader()
            for ticket in self.all_tickets:
                writer.writerow(ticket.prep_payload())
            record.flush()
        self.all_tickets = self.query_tickets()

    def write_to_cancelled_csv(self):
        if not hasattr(self, 'all_cancelled_tickets'):
            self.all_cancelled_tickets = []  # Initialize the list if it doesn't exist

        with open(CANCELLED_TICKETS, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat', 'cancelled_date'])
            writer.writeheader()
            for ticket in self.all_cancelled_tickets:
                if isinstance(ticket, CancelledTicketConfig):  # Ensure correct type
                    writer.writerow(ticket.cancelled_ticket_payload())
                else:
                    print(f"Skipped invalid object in cancelled tickets: {ticket}")

    def get_valid_name(self, prompt):
        while True:
            name = input(prompt).strip().title()
            if len(name) < 3:
                print("Name must have at least 3 characters. Please try again.")
            elif any(char.isdigit() for char in name):
                print("Name cannot contain numbers. Please try again.")
            elif not name.isalpha():
                print("Name cannot contain symbols or special characters. Please try again.")
            else:
                return name

    def book_seat(self):
        if len([ticket for ticket in self.all_tickets if ticket.status == "Active"]) >= 100:
            print('All seats are booked! \nNo more empty seats available!')
            return None
        first_name = self.get_valid_name("Enter Your First Name: ")
        last_name = self.get_valid_name("Enter Your Last Name: ")
        fullname = f"{first_name} {last_name}"

        ticket_number = f'{self.customer_id()}-{self.booking_id()}'
        customer_id = self.customer_id()
        seat_number = self.assign_seat_number()
        window_seat = str(seat_number % 2 == 0)
        booking_time = self.time
        status = 'Active'.title()

        my_ticket = self.config_ticket(customer_id, fullname, ticket_number, seat_number, booking_time, status, window_seat)
        frontend_payload = my_ticket.prep_payload()
        display_payload = f'\nName: {frontend_payload["fullname"]} \nTicket Number: {frontend_payload["ticket_number"]} \nSeat Number: {frontend_payload["seat_number"]} \nWindow Seat: {frontend_payload["window_seat"]}'
        self.all_tickets.append(my_ticket)
        self.write_to_csv()
        print(f'\nHello {list(fullname.split(" "))[0]}! \nYour flight ticket with the following details has been booked successfully!: \n{display_payload}')
        print(f'\nSeats remaining: {100 - len([ticket for ticket in self.all_tickets if ticket.status == "Active"])}')
        return

    def read_tickets(self):
        booked_ticket_number = input('Enter Your Ticket Number: ')
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                print(f'\nCurrent reservation details:\nName: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} ')
                confirm_del = input('\nProceed to Main Menu | Yes/No:').strip().upper()
                if confirm_del == 'YES':
                    return
        print(f'No ticket found with Ticket Number: {booked_ticket_number}')

    def del_tickets(self):
        booked_ticket_number = input('Enter Your Ticket Number: ')
        ticket_found = False
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                ticket_found = True
                print(f'\nAre you Sure You Want to Cancel This Reservation?\n\nName: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} ')
                confirm_del = input('\nType a YES or NO to proceed with reservation cancellation: \n').strip().upper()
                if confirm_del == 'YES':
                    cancelled_ticket = CancelledTicketConfig(
                        customer_id=row.customer_id,
                        fullname=row.fullname,
                        ticket_number=row.ticket_number,
                        seat_number=row.seat_number,
                        booking_time=row.booking_time,
                        status='Cancelled',  # Update status to Cancelled
                        window_seat=row.window_seat,
                        cancelled_date=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                    )
                    # Append the cancelled ticket to a list of cancelled tickets
                    if not hasattr(self, 'all_cancelled_tickets'):
                        self.all_cancelled_tickets = []
                    self.all_cancelled_tickets.append(cancelled_ticket)

                    self.all_tickets.remove(row)
                    self.write_to_csv()
                    self.write_to_cancelled_csv()
                    print(f'Reservation for Ticket Number: {booked_ticket_number} has been cancelled!')
                    print(f'\nSeats remaining: {100 - len([ticket for ticket in self.all_tickets if ticket.status == "Active"])}')
                    return
                else:
                    print('Cancellation aborted.')
                    return

        if not ticket_found:
            print(f'\nNo ticket found with this Ticket Number: {booked_ticket_number}')


    def edit_ticket(self):
        booked_ticket_number = input('Enter Your Ticket Number: ').strip()
        # Flag to check if the ticket is found
        ticket_found = False
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                ticket_found = True
                print(f'Current reservation details:\n'
                      f'Name: {row.fullname}\n'
                      f'Ticket Number: {row.ticket_number}\n'
                      f'Seat Number: {row.seat_number}\n'
                      f'Ticket Status: {row.status}\n'
                      f'Booking Time: {row.booking_time}\n')
                print('\nEnter new details or Press Enter to keep the current details.\n')

                # Get new details from user or retain current details
                new_first_name = input(f'Enter Your First Name [{row.fullname.split(" ")[0]}]: ').strip().title() or \
                                 row.fullname.split(" ")[0]
                new_last_name = input(f'Enter Your Last Name [{row.fullname.split(" ")[1]}]: ').strip().title() or \
                                row.fullname.split(" ")[1]
                row.fullname = f"{new_first_name} {new_last_name}"

                # Update the tickets file
                self.write_to_csv()

                print(f'Reservation for Ticket Number: {booked_ticket_number} has been updated!')
                break  # Exit the loop after finding and updating the ticket

        if not ticket_found:
            print(f'No ticket found with Ticket Number: {booked_ticket_number}')

    def display_seating(self, total_seats=101, seats_per_row=3):
        print("\nAircraft Seating Chart")
        print("=" * (seats_per_row * 5 + 6))

        # Get the list of seat numbers for booked seats
        booked_seats = [int(ticket.seat_number) for ticket in self.all_tickets if ticket.status == 'Active']

        seat_number = 1  # Start seat numbering

        # Loop through rows
        for row in range(1, (total_seats // seats_per_row) + 2):
            row_display = []
            for seat in range(seats_per_row):
                # Check if the seat is booked
                if seat_number in booked_seats:
                    row_display.append(" x ")
                else:
                    row_display.append(f"{seat_number:2} ")
                seat_number += 1

                # Stop when the total seats are exhausted
                if seat_number > total_seats:
                    break

            # Print the row
            print(" | ".join(row_display))

        print("=" * (seats_per_row * 5 + 6))
