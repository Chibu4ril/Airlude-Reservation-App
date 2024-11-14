import random
import time
from datetime import datetime


class CustomerBookingID:
    def __init__(self):
        self.count = 0
        self.booking_digit_count = 0
        self.ticket_number = self.customer_id() + '-' + self.booking_id()

    def customer_id(self):
        #Creating a customer ID - 3
        c_id_range = range(0, 3)
        customerId = []
        while self.count <= 3:
            for i in c_id_range:
                random_range = random.randrange(5)
                customerId.append(i + random_range)
            break
        random_num_gen = ''.join(str(item) for item in customerId )
        return random_num_gen

    def booking_id(self):
        c_id_range = range(0, 5)
        bookingId = []
        while self.booking_digit_count <= 5:
            for i in c_id_range:
                random_range = random.randrange(5)
                bookingId.append(i + random_range)
            break
        random_booking_gen = ''.join(str(item) for item in bookingId)
        return random_booking_gen

    # ticketID = CustomerBookingID()

    def book_seat(self):
        booking_time = datetime.now().strftime('%H:%M:%S')
        booking_date = datetime.now().strftime('%d %m %Y')
        fname = input('First Name: ')
        lname = input('Last Name: ')

        print(fname + ' ' + lname + ' ' + self.ticket_number +' '+ booking_time + ' ' + booking_date )



# custermer id -
# fullname -
# ticket number -
# time created
# status
# seat number
# seat class
# time updated



# def bookingDetails():
#     userName = f'{first_name} {last_name}'
#     bookingItem = [userName, ticket_number,  ticket_type, ]
#     return bookingItem
#
#
# print(bookingDetails())
#
#
# def start_booking():
#     print('                  ')
#     print('Welcome to the ticket booking process!')
#     first_name = input('Enter First Name: ')
#     last_name = input('Enter Last Name: ')
#     ticket_type = int(input('Ticket Class (Press 0 for \"Economy\" or 1 for \"Business\"): '))
#     if ticket_type == 0:
#         ticket_type = 'Economy'
#     else:
#         ticket_type = 'Business Class'
#
#     full_name = first_name + ' ' + last_name
#
#     booking_details = []
#
#     return booking_details
#
#
# try:
#     if booking_request == 'Yes':
#         print('                  ')
#         print(start_booking())
#
#     elif booking_request == 'No':
#         print('                  ')
#         print('Confirm my Reservation?')
#         booking_Id = input('Enter your Ticket Number/Booking Id: ')
#
# except Exception:
#     pass

if __name__ == "__main__":
    print('This is the booking file.')