from booking import Ticketing

# Starting class for the Airline Ticket Reservation System

class Welcome:
    def __init__(self):
        # Initialized with a Ticketing instance and also set the total expected maximumn number of seats to 100
        self.ticketing = Ticketing()
        self.total_seats = 100

    # This method prints a welcome header message to the user.
    def display_welcome_message(self):
        print('\n===========================================================')
        print('    Welcome to Airlude Airline Ticket Reservation System  ')
        print('       You are a ticket away from your destination!!!        ')
        print('      ✈️============================================✈️        \n')

    # This method prints the current status of total available seats vs booked seats.
    def display_seat_info(self):
        print(f'Total Seats Available: {self.total_seats - self.ticketing.counter}')
        print(f'Total Seats Booked: {self.ticketing.counter} \n')

    # This method displays the menu options to the users also and handles their selection.
    def menu(self):
        menu_items = {
            1: "Book a Reservation",
            2: "View a Reservation Details",
            3: "Modify a Reservation",
            4: "Cancel a Reservation",
            5: "View Seat Mapping",
            6: "Exit"
        }
        # Prints each menu item, line by line
        for key, value in menu_items.items():
            print(f'✈ {key} - {value}')

        # Handles user input and validate the selection
        try:
            choice = int(input('\nEnter a selection from 1-6: ').strip())
            if choice < 1 or choice > 6:
                raise ValueError("Selection out of range.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return self.menu()

        actions = {
            1: self.ticketing.book_seat,
            2: self.ticketing.read_tickets,
            3: self.ticketing.edit_ticket,
            4: self.ticketing.del_tickets,
            5: self.ticketing.display_seating,
            6: lambda: (print("Thank you for using Airlude Airline Reservation System! Goodbye!"), exit())
        }

        print(f'\n✈ {menu_items[choice]} - SELECTED\n')
        actions[choice]()
        if choice != 6:
            self.main()

    def main(self):
        self.display_welcome_message()
        self.display_seat_info()
        self.menu()


if __name__ == "__main__":
    Welcome().main()

