print('Welcome to Airlude Airline Ticket Reservation System')
print('You are a ticket away from your destination!!!')

import sys

from db_script import Database

DB = Database()

print(DB.read_file())