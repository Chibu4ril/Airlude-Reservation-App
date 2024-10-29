

print('=========================================================')
print('#    Welcome to Airlude Airline Ticket Reservation System ')
print('#    You are a ticket away from your destination!!! ')

print('==========================================================')
print('                  ')


import sys

from db_script import Database


print('What would you want to do today?')

print('Book a Ticket?')
booking_request = input('Type Yes or No: ')

def start_booking():
    print('                  ')
    print('Welcome to the ticket booking process!')
    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    ticket_type = int(input('Ticket Class (Press 0 for \"Economy\" or 1 for \"Business\"): '))
    if ticket_type  == 0:
        ticket_type = 'Economy'
    else:
        ticket_type = 'Business Class'

    full_name = first_name + ' ' + last_name
    

    booking_details =

    return booking_details

try:
    if booking_request == 'Yes':
        print('                  ')
        print(start_booking())

    elif booking_request == 'No':
        print('                  ')
        print('Confirm my Reservation?')
        booking_Id = input('Enter your Ticket Number/Booking Id: ')

except Exception:
    pass





#
# DB = Database()
#
# print(DB.read_file())