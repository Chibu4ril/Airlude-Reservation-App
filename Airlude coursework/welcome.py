
import sys
import time






class Welcome:
    def __init__(self):
        self.total_seats = 100
        self.booked_seat = 0

    def loader(self, duration):
        spinner = ['|✈', '/✈', '-✈', '\\✈']
        end_timer = time.time() + duration
        while time.time() < end_timer:
            for items in spinner:
                sys.stdout.write('r' + items)
                sys.stdout.flush()
                time.sleep(0.1)
        print('\nLet"s Go!!! ✈')

    def menuList(self):
        menuItems = ['✈ 1 - Book a Reservation', '✈ 2 - Cancel My Reservation ', '✈ 3 - Modify My Reservation',                         '✈ 4 - View My Reservation Details', '✈ 5 - Exit']
        print(f'{menuItems[0]} \n{menuItems[1]} \n{menuItems[2]} \n{menuItems[3]} \n{menuItems[4]}')
        print('')
        user_request = int(input('Make a selection from 1-5: '))
        try:
            user_request <= len(menuItems)
        except WrongInput as error:
            selection_error(error)
        else:
            if user_request == 1:
                 book_seat()
            elif user_request == 2:
                cancel_reserve()
            elif user_request == 3:
                modify_reserve()
            elif user_request == 4:
                view_reserve()
            elif user_request == 5:
                quit()
        finally:
            self.loader(5)


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

