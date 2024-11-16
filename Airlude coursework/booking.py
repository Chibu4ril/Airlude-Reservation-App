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
            print('All seats are booked! \nNo more empty seats available!')
            return None
        fullname = f'{input('Enter Your First Name: ').title()} {input('Enter Your Last Name: ').title()}'
        ticket_number = f'{self.customer_id()}-{self.booking_id()}'
        customer_id = self.customer_id()
        seat_number = len([ticket for ticket in self.all_tickets if ticket.status == 'active']) + 1
        booking_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        status = 'active'.title()
        ticket_type = 'Economy'
        window_seat =  str(seat_number % 2 ==0)
        my_ticket = self.config_ticket(customer_id, fullname, ticket_number, seat_number, booking_time, status, ticket_type, window_seat)
        frontend_payload = my_ticket.prep_payload()
        display_payload = f'\nName: {frontend_payload['fullname']} \nTicket Number: {frontend_payload['ticket_number']} \nSeat Number: {frontend_payload['seat_number']} \nWindow Seat: {frontend_payload['window_seat']}'
        self.all_tickets.append(my_ticket)
        with open(TICKETS_FILE, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'ticket_type', 'window_seat'])
            writer.writeheader()
            for ticket in self.all_tickets:
                writer.writerow(ticket.prep_payload())
        print(f'\nHello {list(fullname.split(' '))[0]}! \nYour flight ticket with the following details has been booked successfully!: \n{display_payload}')
        return my_ticket

    def read_tickets(self):
        booked_ticket_number = input('Enter Your Ticket Number: ')
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                print(f'Name: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} ')

    def del_tickets(self):
        booked_ticket_number = input('Enter Your Ticket Number: ')
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                print(f'Are you Sure You Want to Cancel This Reservation?\nName: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} ')
                confirm_del = input('Type a YES or NO to proceed with reservation cancellation: ').strip().upper()
                if confirm_del == 'YES':
                    self.all_tickets.remove(row)
                    with open(TICKETS_FILE, mode='w', newline='') as record:
                        writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'ticket_type', 'window_seat'])
                        writer.writeheader()
                        for ticket in self.all_tickets:
                            writer.writerow(ticket.prep_payload())
                    print(f'Reservation for Ticket Number: {booked_ticket_number} has been cancelled!')
                    return
                else:
                    print('Cancellation aborted.')
                    return
            else:
                print(f'No ticket found with this Ticket Number: {booked_ticket_number}')
                break


    def edit_ticket(self):
        booked_ticket_number = input('Enter Your Ticket Number: ')
        for row in self.all_tickets:
            if row.ticket_number == booked_ticket_number:
                print(f'Current reservation details:\nName: {row.fullname} \nTicket Number: {row.ticket_number} \nSeat Number: {row.seat_number}\nTicket Status: {row.status}\nBooking Time: {row.booking_time} \n')
                print('Enter new details or Press Enter to keep the current details.\n')
                new_fullname = f'{input(f'Enter Your First Name[{list(row.fullname.split(' '))[0]}]: ').title().strip()} {input(f'Enter Your Last Name[{list(row.fullname.split(' '))[1]}]: ').title().strip()}' or row.fullname
                row.fullname = new_fullname
                with open(TICKETS_FILE, mode='w', newline='') as record:
                    writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'ticket_type', 'window_seat'])
                    writer.writeheader()
                    for ticket in self.all_tickets:
                        writer.writerow(ticket.prep_payload())
                print(f'Reservation for Ticket Number: {booked_ticket_number} has been updated!')
                return
            else:
                print(f'No ticket found with this Ticket Number: {booked_ticket_number}')
                break







