import csv
from datetime import datetime
from ticketconfig import TicketConfig
from ticketconfig import CancelledTicketConfig
from api import CSVQuery
import random

TICKETS_FILE = 'flight_db.csv'
CANCELLED_TICKETS = "cancelled_tickets.csv"

class Ticketing:
    """
    Handles the ticketing operations including booking, editing, cancellation,
    and displaying seating arrangements for an airline reservation system.
    """
    def __init__(self):
        # Load ticket data from CSV
        self.csv_query_instance = CSVQuery()
        self.all_tickets = CSVQuery().query_tickets()
        self.all_cancelled_tickets = CSVQuery().query_cancelled_tickets()

        # Ticket configuration and initialization
        self.config_ticket = TicketConfig
        self.cancelled_ticket_config = CancelledTicketConfig
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        # Count active tickets
        self.counter = len([ticket for ticket in self.all_tickets if ticket.status == 'Active'])

        # Define lambda methods for writing updates to CSV
        self.delete = self.delete = lambda: self.csv_query_instance.write_to_cancelled_csv(self.all_cancelled_tickets)
        self.write = lambda: self.csv_query_instance.write_to_csv(self.all_tickets)

        # Generate unique customer ID
        self.customer_id = self.customer_id()

    def assign_seat_number(self):
        # Assign a seat number by checking for taken seats and filling up any gaps.

        taken_seats = [int(ticket.seat_number) for ticket in self.all_tickets if ticket.status == 'Active']

        next_seat_number = 1
        while next_seat_number in taken_seats:
            next_seat_number += 1

        # If any seat number is skipped, find the first missing number
        missing_seats = sorted(set(range(1, next_seat_number)) - set(taken_seats))
        if missing_seats:
            next_seat_number = missing_seats[0]

        # Check and assign the next available seat number
        if any(ticket.seat_number == str(next_seat_number) for ticket in self.all_tickets):
            print(f"Seat Number {next_seat_number} is already taken. Checking for the next available seat...")
            next_seat_number = len([ticket for ticket in self.all_tickets if ticket.status == 'Active']) + 1
            # A recursive or additional logic to find the next available seat

        return next_seat_number

    @classmethod
    def customer_id(cls):
        # Generate a unique customer ID.
        # Create a string of 3 random numbers in the range 0-4
        return ''.join(str(random.randint(0, 4)) for _ in range(3))

    @classmethod
    def booking_id(cls):
        # Generate a unique booking ID.
        # Create a string of 5 random numbers in the range 0-4
        return ''.join(str(random.randint(0, 4)) for _ in range(5))

    # this method validates the name input to ensure it has at least 3 characters and contains no numbers or special characters.
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
        # Book a new seat for a passenger.
        if len([ticket for ticket in self.all_tickets if ticket.status == "Active"]) >= 100:
            print('All seats are booked! \nNo more empty seats available!')
            return None


        first_name_input = self.get_valid_name("Enter Your First Name: ")
        last_name_input = self.get_valid_name("Enter Your Last Name: ")
        fullname_combined = f"{first_name_input} {last_name_input}"

        generated_ticket_number = f'{self.customer_id}-{self.booking_id()}'
        customer_id = self.customer_id
        seat_number = self.assign_seat_number()

        def window_seat_checker(seat_number):
            # Check if a given seat number is a window seat.
            if (seat_number - 1) % 3 == 0:
                return "This is a Window seat"
            else:
                return "Not a Window Seat"

        window_seat = window_seat_checker(seat_number)
        booking_time = self.time
        status = 'Active'.title()



        my_ticket = self.config_ticket(customer_id, fullname_combined, generated_ticket_number, seat_number, booking_time, status, window_seat)
        frontend_payload = my_ticket.prep_payload()
        display_payload = f'\nName: {frontend_payload["fullname"]} \nTicket Number: {frontend_payload["ticket_number"]} \nSeat Number: {frontend_payload["seat_number"]} \nWindow Seat: {frontend_payload["window_seat"]} \nBooking Time: {frontend_payload["booking_time"]}'
        self.all_tickets.append(my_ticket)
        self.write()
        print(f'\nHello {list(fullname_combined.split(" "))[0]}! \nYour flight ticket with the following details has been booked successfully!: \n{display_payload}')
        print(f'\nSeats remaining: {100 - len([ticket for ticket in self.all_tickets if ticket.status == "Active"])}')
        return

    def read_tickets(self):
        # View the details of a booked ticket by entering the ticket number.
        booked_ticket_number = input('Enter Your Ticket Number: ')
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                print(f'\nCurrent reservation details:\n\nName: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} ')
            else:
                print(f'No ticket found with Ticket Number: {booked_ticket_number}')

    def del_tickets(self):
        # Cancel an existing ticket by entering the ticket number.
        # Moves the ticket from active tickets to cancelled tickets.
        booked_ticket_number = input('Enter Your Ticket Number: ').strip()
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
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
                    self.write()
                    self.delete()
                    print(f'Reservation for Ticket Number: {booked_ticket_number} has been cancelled!')
                    print(f'\nSeats remaining: {100 - len([ticket for ticket in self.all_tickets if ticket.status == "Active"])}')
                    return
                else:
                    print('Cancellation aborted.')

        print(f'\nNo ticket found with this Ticket Number: {booked_ticket_number}')


    def edit_ticket(self):
        # Edit passenger details of an existing ticket by entering the ticket number.
        booked_ticket_number = input('Enter Your Ticket Number: ').strip()
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
                new_first_name = input(f'New First Name [{row.fullname.split(" ")[0]}]: ').strip().title() or \
                                 row.fullname.split(" ")[0]
                new_last_name = input(f'New Last Name [{row.fullname.split(" ")[1]}]: ').strip().title() or \
                                row.fullname.split(" ")[1]
                row.fullname = f"{new_first_name} {new_last_name}"

                self.write()

                print(f'Reservation for Ticket Number: {booked_ticket_number} has been updated!')
                break

        if not ticket_found:
            print(f'No ticket found with Ticket Number: {booked_ticket_number}')

    def display_seating(self, total_seats=100, seats_per_row=3):
        # Display the seating arrangement of the aircraft.
        # Shows booked and available seats along with window seat indicators.
        print("\nAircraft Seats")
        print("=" * (seats_per_row * 5 + 6))
        print("w - represents window seat\n")

        booked_seats = [int(ticket.seat_number) for ticket in self.all_tickets if ticket.status == 'Active']

        seat_number = 1

        for row in range(1, (total_seats // seats_per_row) + 2):
            row_display = []
            for seat in range(seats_per_row):
                is_window_seat = seat_number % seats_per_row == 1

                if seat_number in booked_seats:
                    if is_window_seat:
                        row_display.append(" x-w")
                    else:
                        row_display.append(" x ")
                else:
                    if is_window_seat:
                        row_display.append(f"{seat_number:2}-w")
                    else:
                        row_display.append(f"{seat_number:2} ")
                seat_number += 1

                if seat_number > total_seats:
                    break
            print(" | ".join(row_display))

        print("=" * (seats_per_row * 5 + 6))
