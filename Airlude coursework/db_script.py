import csv
import os
import random
import time

class Database:
    def __init__(self):
        # print('Welcome')
        self.my_csv_file = 'flight_db.csv'
        self.customer_details = CustomerBookingID()

    def csv_record_checker(self):
        records = []
        try:
            if not os.path.isfile(self.my_csv_file):
                with open(self.my_csv_file, mode='r') as file:
                    db_reader = csv.DictReader(file)
                    records = list(db_reader)
        except FileNotFoundError:
            print('No record found, start booking.')
        return records


    # Defining my csv file for i/o

    def write_file(self):
        if not os.path.isfile(self.my_csv_file):
            with open(self.my_csv_file, mode='w', newline='') as customer_itinerary:
                itinerary_rows = csv.writer(customer_itinerary, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
                itinerary_rows.writerow(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7'])

    def read_file(self):
        with open(self.my_csv_file, mode='r') as customer_itinerary:
            itinerary_rows = csv.reader(customer_itinerary, delimiter=',')
            for rows in itinerary_rows:
                # print(rows)
                return rows


class CustomerBookingID:
    def __init__(self):
        self.count = 0
        self.booking_digit_count = 0
        self.ticket_number = self.customer_id() + '-' + self.booking_id()

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

    # ticketID = CustomerBookingID()

    def book_seat(self):
        fname = input('First Name: ')
        lname = input('Last Name: ')
        fullname = fname + ' ' + lname
        customer_id = self.customer_id()
        ticket_id = self.ticket_number





# #
# DB = Database()
#
# DB.write_file()
#
# print(DB.read_file())