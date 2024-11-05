import csv
import os


class Database:
    def __init__(self):
        # print('Welcome')
        self.my_csv_file = 'flight_db.csv'

    # Defining my csv file for i/o
   

    def write_file(self):
        with open(self.my_csv_file, mode='w') as customer_itinerary:
            itinerary_rows = csv.writer(customer_itinerary, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
            itinerary_rows.writerow([2, 'mARK', '2399505', '123', 'active', 'economy', 'Window Seat'])

    def read_file(self):
        with open(self.my_csv_file, mode='r') as customer_itinerary:
            itinerary_rows = csv.reader(customer_itinerary, delimiter=',')
            for rows in itinerary_rows:
                # print(rows)
                return rows




# #
# DB = Database()
#
# DB.write_file()
#
# print(DB.read_file())