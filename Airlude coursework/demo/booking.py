import csv
from datetime import datetime
from ticketconfig import TicketConfig
import random

TICKETS_FILE = 'flight_db.csv'

class Ticketing:
    def __init__(self):
        self.all_tickets = self.query_tickets()
        self.config_ticket = TicketConfig


    def count_seats_available(self):
        return len(self.all_tickets)

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

    def assign_seat_number(self):
        while True:
            # Calculate the next seat number
            next_seat_number = len([ticket for ticket in self.all_tickets if ticket.status == 'Active'])
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
        if len([ticket for ticket in self.all_tickets if ticket.status == 'Active']) >= 100:
            print('All seats are booked! \nNo more empty seats available!')
            return None
        first_name = self.get_valid_name("Enter Your First Name: ")
        last_name = self.get_valid_name("Enter Your Last Name: ")
        fullname = f"{first_name} {last_name}"

        ticket_number = f'{self.customer_id()}-{self.booking_id()}'
        customer_id = self.customer_id()
        seat_number = self.assign_seat_number()
        window_seat = str(seat_number % 2 == 0)
        booking_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        status = 'Active'.title()

        my_ticket = self.config_ticket(customer_id, fullname, ticket_number, seat_number, booking_time, status, window_seat)
        frontend_payload = my_ticket.prep_payload()
        display_payload = f'\nName: {frontend_payload["fullname"]} \nTicket Number: {frontend_payload["ticket_number"]} \nSeat Number: {frontend_payload["seat_number"]} \nWindow Seat: {frontend_payload['window_seat']}'
        self.all_tickets.append(my_ticket)
        self.write_to_csv()
        self.count_seats_available()
        print(f'\nHello {list(fullname.split(' '))[0]}! \nYour flight ticket with the following details has been booked successfully!: \n{display_payload}')
        return my_ticket

    def read_tickets(self):
        booked_ticket_number = input('Enter Your Ticket Number: ')
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                print(f'Name: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} ')
                return
        print(f'No ticket found with Ticket Number: {booked_ticket_number}')

    def del_tickets(self):
        booked_ticket_number = input('Enter Your Ticket Number: ')
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                print(f'Are you Sure You Want to Cancel This Reservation?\nName: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} ')
                confirm_del = input('\nType a YES or NO to proceed with reservation cancellation: \n').strip().upper()
                if confirm_del == 'YES':
                    self.all_tickets.remove(row)
                    self.write_to_csv()
                    print(f'Reservation for Ticket Number: {booked_ticket_number} has been cancelled!')
                    print(f'\nSeats remaining: {100 - len([ticket for ticket in self.all_tickets if ticket.status == 'Active'])}')
                    return
                else:
                    print('Cancellation aborted.')
                    return

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
                print('Enter new details or Press Enter to keep the current details.\n')

                # Get new details from user or retain current details
                new_first_name = input(f'Enter Your First Name [{row.fullname.split(" ")[0]}]: ').strip().title() or \
                                 row.fullname.split(" ")[0]
                new_last_name = input(f'Enter Your Last Name [{row.fullname.split(" ")[1]}]: ').strip().title() or \
                                row.fullname.split(" ")[1]
                row.fullname = f"{new_first_name} {new_last_name}"

                # Update the tickets file
                with open(TICKETS_FILE, mode='w', newline='') as record:
                    writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat'])
                    writer.writeheader()
                    for ticket in self.all_tickets:
                        writer.writerow(ticket.prep_payload())

                print(f'Reservation for Ticket Number: {booked_ticket_number} has been updated!')
                break  # Exit the loop after finding and updating the ticket

        if not ticket_found:
            print(f'No ticket found with Ticket Number: {booked_ticket_number}')








