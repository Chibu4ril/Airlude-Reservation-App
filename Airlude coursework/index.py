from booking import Ticketing

class Welcome:
    def __init__(self):
        self.total_seats = 100
        self.process = Ticketing()

    def menu(self):
        menu_items = ['1 - Book a Reservation', '2 - Cancel My Reservation ', '3 - Modify My Reservation',
                      '4 - View My Reservation Details', '5 - Exit']
        print(f'✈ {menu_items[0]} \n✈ {menu_items[1]} \n✈ {menu_items[2]} \n✈ {menu_items[3]} \n✈ {menu_items[4]}')
        print('')

        choice = int(input('Enter a selection from 1-5: '))

        if choice  == 1:
            print(menu_items[0] + ' ' + '- SELECTED')
            print(' ')
            self.process.book_seat()
        else:
            print('You entered an invalid choice. \n Please Try Again')


    def main(self):
        print('                  ')
        print('===========================================================')
        print('    Welcome to Airlude Airline Ticket Reservation System  ')
        print('       You are a ticket away from your destination!!!        ')
        print('      ✈️============================================✈️        ')
        print('                  ')
        print(f'Total Seats Available: {self.total_seats}')
        print(f'Total Seats Booked: {self.total_seats}')
        print(' ')

        print('What would you want to do today?')
        self.menu()


# ========================= Initializer ==================
if __name__ == "__main__":
    start = Welcome()
    start.main()


