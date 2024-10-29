import csv
import sys

from welcome import *
# from
class Database:
    def __init__(self):
        # print('Welcome')
        pass

    def write_file(self):
        with open('flight_db.csv', mode='w') as customer_itinerary:
            itinerary_rows = csv.writer(customer_itinerary, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
            itinerary_rows.writerow([2, 'Innocent', '2399505', '123', 'active', 'economy', 'Window Seat'])

    def read_file(self):
        with open('flight_db.csv', mode='r') as customer_itinerary:
            itinerary_rows = csv.reader(customer_itinerary, delimiter=',')
            for rows in itinerary_rows:
                # print(rows)
                return rows



