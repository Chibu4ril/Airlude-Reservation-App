from booking import Ticketing

class Welcome:
    def __init__(self):
        self.total_seats = 100
        self.create_ticket = Ticketing()
        self.delete_ticket = Ticketing()
        self.read_ticket = Ticketing()
        self.update_ticket = Ticketing()

    def menu(self):
        menu_items = ['1 - Book a Reservation', '2 - Modify a Reservation', '3 - Cancel a Reservation', '4 - View a Reservation Details', '5 - View Seat Mapping', '6 - Exit']
        print(f'✈ {menu_items[0]} \n✈ {menu_items[1]} \n✈ {menu_items[2]} \n✈ {menu_items[3]} \n✈ {menu_items[4]} \n✈ {menu_items[5]}')
        print('')

        choice = int(input('Enter a selection from 1-5: '))

        if choice  == 1:
            print(menu_items[0] + ' ' + '- SELECTED \n')
            self.create_ticket.book_seat()
        elif choice == 2:
            print(menu_items[1] + ' ' + '- SELECTED \n')
            self.update_ticket.edit_ticket()
        elif choice == 3:
            print(menu_items[2] + ' ' + '- SELECTED \n')
            self.delete_ticket.del_tickets()
        elif choice == 4:
            print(menu_items[3] + ' ' + '- SELECTED \n')
            self.read_ticket.read_tickets()
        else:
            print('You entered an invalid choice. \nPlease Try Again')


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


