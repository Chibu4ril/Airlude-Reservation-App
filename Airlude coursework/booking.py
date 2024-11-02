first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')
ticket_type = int(input('Ticket Class (Press 0 for \"Economy\" or 1 for \"Business\"): '))


import random

class CustomerBookingID:
    def __init__(self):
        self.count = 0
        self.booking_digit_count = 0

    def customer_id(self):
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

ticketID = CustomerBookingID()

ticket_number = ticketID.customer_id() + '-' + ticketID.booking_id()


def bookingDetails():
    userName = f'{first_name} {last_name}'
    bookingItem = [userName, ticket_number,  ticket_type, ]
    return bookingItem


print(bookingDetails())