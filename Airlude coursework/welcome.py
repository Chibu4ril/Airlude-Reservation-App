import os.path
import sys
import time
from booking import CustomerBookingID
from db_script import Database


class Welcome:
    def __init__(self):
        self.total_seats = 100
        self.booker = CustomerBookingID()
        self.db = Database()



    def selection_error(self):
        print('Wrong input!')

    def loader(self, duration):
        for i, items in enumerate(duration):
            print(f'{items}...', end="", flush=True)
            time.sleep(1)
            print('Done ')

    def menu_list(self):
        menu_items = ['✈ 1 - Book a Reservation', '✈ 2 - Cancel My Reservation ', '✈ 3 - Modify My Reservation',                         '✈ 4 - View My Reservation Details', '✈ 5 - Exit']
        print(f'{menu_items[0]} \n{menu_items[1]} \n{menu_items[2]} \n{menu_items[3]} \n{menu_items[4]}')
        print('')
        # print(f'{'-' * 30}')
        choice = input('Enter a selection from 1-5: ')
        # print(f'{'-' * 30}')

        try:
            choice <= len(menu_items)
        except NameError as error:
            # selection_error(error)
            print('Heelo')
        else:
            if choice == '1':
                print(menu_items[0])
                self.loader(["Processing"])
                self.booker.book_seat()
                # self.book_again()
            elif choice == '2':
                print(menu_items[1])
                # cancel_reserve()
            elif choice == '3':
                print(menu_items[2])
                # modify_reserve()
            elif choice == '4':
                print(menu_items[3])
                # view_reserve()
            elif choice == '5':

                print(menu_items[4])
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
        print('      ✈️============================================✈️        ')
        print('                  ')
        # End of header section

        print(f'Total Seats Available: {self.total_seats}')
        print(f'Total Seats Booked: {self.total_seats - self.db.db_record_checker() }')
        print(' ')

        print('What would you want to do today?')
        self.menu_list()


        # ========================= footer sections =======================
        print(' ')
        print('------------------------> © 2024 All Rights Reserved. Airlude <------------------------------')




# def selection():
#     if len(menu_items) <= menu_items():
#         print('Yes')





# ========================= Initializer ==================
if __name__ == "__main__":
    start = Welcome()
    start.main()


