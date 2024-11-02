
import sys


total_seats = 100
booked_seat = 0


def selection():
    if len(menuItems) <= menuList():
        print('Yes')





def menuList():
    global menuItems
    menuItems = ['✈ 1 - Book a Reservation', '✈ 2 - Cancel My Reservation ', '✈ 3 - Modify My Reservation', '✈ 4 - View My Reservation Details', '✈ 5 - Exit']
    print(f'{menuItems[0]} \n{menuItems[1]} \n{menuItems[2]} \n{menuItems[3]} \n{menuItems[4]}')
    print ('')
    user_request = int(input('Make a selection from 1-5: '))
    if user_request <= len(menuItems):
        

def main():
    # Welcome header section
    print('                  ')
    print('===========================================================')
    print('    Welcome to Airlude Airline Ticket Reservation System  ')
    print('       You are a ticket away from your destination!!!        ')
    print('       ✈️============================================✈️        ')
    print('                  ')
    # End of header section

    print(f'Total Seats Available: {total_seats}')
    print(f'Total Seats Booked: {booked_seat}')
    print(' ')

    print('What would you want to do today?')
    menuList()




    # ========================= footer sections =======================
    print(' ')
    print('------------------------> © 2024 All Rights Reserved. Airlude <------------------------------')


# ========================= Initializer ==================
if __name__ == "__main__":
    main()

