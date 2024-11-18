import tkinter as tk
from tkinter import ttk
from random import choice
from booking import Ticketing

class WelcomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Airlude Airline Ticket Reservation System")
        self.root.geometry("600x400")
        self.count_tickets = Ticketing()
        self.total_seats = 100
        self.create_ticket = Ticketing()
        self.delete_ticket = Ticketing()
        self.read_ticket = Ticketing()
        self.update_ticket = Ticketing()
        self.choice = choice

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_label = ttk.Label(
            self.root,
            text="Welcome to Airlude Airline Ticket Reservation System",
            font=("Helvetica", 14),
            anchor="center"
        )
        header_label.grid(row=0, column=0, columnspan=2, pady=10)

        subheader_label = ttk.Label(
            self.root,
            text="You are a ticket away from your destination!",
            font=("Helvetica", 10)
        )
        subheader_label.grid(row=1, column=0, columnspan=2)

        # Seats info
        self.available_seats_label = ttk.Label(
            self.root,
            text=f"Total Seats Available: {self.total_seats - self.count_seats_available()}",
            font=("Helvetica", 10)
        )
        self.available_seats_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.booked_seats_label = ttk.Label(
            self.root,
            text=f"Total Seats Booked: {self.count_seats_available()}",
            font=("Helvetica", 10)
        )
        self.booked_seats_label.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Menu Buttons
        buttons = [
            ("Book a Reservation", self.book_reservation),
            ("Modify a Reservation", self.modify_reservation),
            ("Cancel a Reservation", self.cancel_reservation),
            ("View a Reservation Details", self.view_reservation),
            ("View Seat Mapping", self.view_seat_mapping),
            ("Exit", self.exit_system),
        ]

        for i, (text, command) in enumerate(buttons, start=3):
            btn = ttk.Button(self.root, text=text, command=command)
            btn.grid(row=i, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

    def count_seats_available(self):
        tickets = 0
        for rows in self.count_tickets.all_tickets:
            tickets += 1
        return tickets

    def update_seats_info(self):
        self.available_seats_label.config(
            text=f"Total Seats Available: {self.total_seats - self.count_seats_available()}"
        )
        self.booked_seats_label.config(
            text=f"Total Seats Booked: {self.count_seats_available()}"
        )

    # Button Command Functions
    def book_reservation(self):
        self.create_ticket.book_seat()
        self.update_seats_info()

    def modify_reservation(self):
        self.update_ticket.edit_ticket()
        self.update_seats_info()

    def cancel_reservation(self):
        self.delete_ticket.del_tickets()
        self.update_seats_info()

    def view_reservation(self):
        self.read_ticket.read_tickets()

    def view_seat_mapping(self):
        self.count_tickets.print_window_seats()

    def exit_system(self):
        self.root.quit()

# ========================= Initializer ==================
if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeGUI(root)
    root.mainloop()
