from random import choice

from booking import Ticketing

class Welcome:
    def __init__(self):
        self.count_tickets = Ticketing()
        self.total_seats = 100
        self.create_ticket = Ticketing()
        self.delete_ticket = Ticketing()
        self.read_ticket = Ticketing()
        self.update_ticket = Ticketing()
        self.choice = choice

    def menu(self):
        menu_items = ['1 - Book a Reservation', '2 - Modify a Reservation', '3 - Cancel a Reservation', '4 - View a Reservation Details', '5 - View Seat Mapping', '6 - Exit']
        print(f'✈ {menu_items[0]} \n✈ {menu_items[1]} \n✈ {menu_items[2]} \n✈ {menu_items[3]} \n✈ {menu_items[4]} \n✈ {menu_items[5]}')
        print('')

        try:
            self.choice = int(input('Enter a selection from 1-6: ').strip())
            if self.choice < 1 or self.choice > 6:
                print("Invalid selection. Please enter a number between 1 and 6.")
                start.main()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            start.main()

        if self.choice  == 1:
            print(menu_items[0] + ' ' + '- SELECTED \n')
            self.create_ticket.book_seat()
        elif self.choice == 2:
            print(menu_items[1] + ' ' + '- SELECTED \n')
            self.update_ticket.edit_ticket()
        elif self.choice == 3:
            print(menu_items[2] + ' ' + '- SELECTED \n')
            self.delete_ticket.del_tickets()
        elif self.choice == 4:
            print(menu_items[3] + ' ' + '- SELECTED \n')
            self.read_ticket.read_tickets()
        else:
            print('You entered an invalid choice. \nPlease Try Again')


    def main(self):
        print('\n===========================================================')
        print('    Welcome to Airlude Airline Ticket Reservation System  ')
        print('       You are a ticket away from your destination!!!        ')
        print('      ✈️============================================✈️        \n')
        def count_seats_available():
            tickets = 0
            for rows in self.count_tickets.all_tickets:
                tickets = tickets + 1
                # print(f'{tickets}')
            return tickets
        print(f'Total Seats Available: {self.total_seats - count_seats_available()}')
        print(f'Total Seats Booked: {count_seats_available()}')
        print(' ')

        print('What would you want to do today?')
        self.menu()


# ========================= Initializer ==================
if __name__ == "__main__":
    start = Welcome()
    start.main()


