from random import choice
from booking import Ticketing

class Welcome:
    def __init__(self):
        self.count_tickets = Ticketing().counter
        self.total_seats = 100
        self.create_ticket = Ticketing()
        self.delete_ticket = Ticketing()
        self.read_ticket = Ticketing()
        self.update_ticket = Ticketing()
        self.ticket_mapping = Ticketing()
        self.choice = choice



    def menu(self):
        menu_items = ['1 - Book a Reservation', '2 - View a Reservation Details', '3 - Modify a Reservation', '4 - Cancel a Reservation', '5 - View Seat Mapping', '6 - Exit']
        for item in menu_items:
            print(f'✈ {item} ')
        print('')

        try:
            self.choice = int(input('Enter a selection from 1-6: ').strip())
            if self.choice < 1 or self.choice > 6:
                print("Invalid selection. Please enter a number between 1 and 6.")
                self.main()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.main()

        if self.choice  == 1:
            print(menu_items[0] + ' - SELECTED \n')
            self.create_ticket.book_seat()
        elif self.choice == 2:
            print(menu_items[1] + ' - SELECTED \n')
            self.read_ticket.read_tickets()

        elif self.choice == 3:
            print(menu_items[2] + '- SELECTED \n')
            self.update_ticket.edit_ticket()

        elif self.choice == 4:
            print(menu_items[3] + ' - SELECTED \n')
            self.delete_ticket.del_tickets()

        elif self.choice == 5:
            print(menu_items[4] + ' - SELECTED \n')
            self.ticket_mapping.display_seating()
        elif self.choice == 6:
            print("Thank you for using Airlude Airline Ticket Reservation System!")
            exit()
        else:
            print('You entered an invalid choice. \nPlease Try Again')
        self.main()


    def main(self):
        print('\n===========================================================')
        print('    Welcome to Airlude Airline Ticket Reservation System  ')
        print('       You are a ticket away from your destination!!!        ')
        print('      ✈️============================================✈️        \n')


        print(f'Total Seats Available: {self.total_seats - self.count_tickets }')
        print(f'Total Seats Booked: {self.count_tickets} \n')

        print('What would you like to do today?')
        self.menu()




# ========================= Initializer ==================
if __name__ == "__main__":
    start = Welcome()
    start.main()


