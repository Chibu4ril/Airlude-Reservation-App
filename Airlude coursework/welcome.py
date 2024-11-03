
import sys
import time
from booking import CustomerBookingID






class Welcome:
    def __init__(self):
        self.total_seats = 100
        self.booked_seat = 0
        self.booker = CustomerBookingID()

    def selection_error(self):
        print('Wrong input!')
    def loader(self, duration):
        for i, items in enumerate(duration):
            print(f'{items}...', end="", flush=True)
            time.sleep(1)
            print('Done ')

    def menuList(self):
        menuItems = ['✈ 1 - Book a Reservation', '✈ 2 - Cancel My Reservation ', '✈ 3 - Modify My Reservation',                         '✈ 4 - View My Reservation Details', '✈ 5 - Exit']
        print(f'{menuItems[0]} \n{menuItems[1]} \n{menuItems[2]} \n{menuItems[3]} \n{menuItems[4]}')
        print('')
        # print(f'{'-' * 30}')
        user_request = int(input('Enter a selection from 1-5: '))
        # print(f'{'-' * 30}')

        try:
            user_request <= len(menuItems)
        except NameError as error:
            selection_error(error)
            print('Heelo')
        else:
            if user_request == 1:
                print(menuItems[0])
                self.loader(["Processing"])
                self.booker.book_seat()
                self.book_again()
            elif user_request == 2:
                print(menuItems[1])
                cancel_reserve()
            elif user_request == 3:
                print(menuItems[2])
                modify_reserve()
            elif user_request == 4:
                print(menuItems[3])
                view_reserve()
            elif user_request == 5:
                print(menuItems[4])
                quit()
        finally:
            self.loader(["Loading Data", "Processing"])
            print(' ')
            print('Thank you for using Airlude today.')
            self.main()


    def main(self):
        # Welcome header section
        print('                  ')
        print('===========================================================')
        print('    Welcome to Airlude Airline Ticket Reservation System  ')
        print('       You are a ticket away from your destination!!!        ')
        print('       ✈️============================================✈️        ')
        print('                  ')
        # End of header section

        print(f'Total Seats Available: {self.total_seats}')
        print(f'Total Seats Booked: {self.booked_seat}')
        print(' ')

        print('What would you want to do today?')
        self.menuList()


        # ========================= footer sections =======================
        print(' ')
        print('------------------------> © 2024 All Rights Reserved. Airlude <------------------------------')




def selection():
    if len(menuItems) <= menuList():
        print('Yes')








# ========================= Initializer ==================
if __name__ == "__main__":
    start = Welcome()
    start.main()

