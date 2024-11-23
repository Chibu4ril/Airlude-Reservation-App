import csv
import tkinter as tk
from tkinter import ttk
from bookinggui import Ticketing
from datetime import datetime
from ticketconfig import TicketConfig
import random

TICKETS_FILE = 'flight_db.csv'

class WelcomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="white")
        self.root.title("Airlude Airline Ticket Reservation System")
        self.root.geometry("1000x550")
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.all_tickets = self.query_tickets()
        self.config_ticket = TicketConfig




        # Ticketing logic
        self.ticket_manager = Ticketing()
        self.total_seats = 100

        # Initialize UI
        self.setup_style()
        self.create_layout()
        self.create_widgets()
        self.update_seats_info()

    def query_tickets(self):
        all_tickets = []
        try:
            with open(TICKETS_FILE, mode='r') as records:
                parse = csv.DictReader(records)
                all_tickets = [TicketConfig.payload_unwrapper(row) for row in parse]
        except FileNotFoundError:
            with open(TICKETS_FILE, mode='w', newline='') as record:
                writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat'])
                writer.writeheader()
            print('No record found!')
        return all_tickets

    def assign_seat_number(self):
        while True:
            # Calculate the next seat number
            next_seat_number = len([ticket for ticket in self.all_tickets if ticket.status == 'Active']) + 1
            # Check if the seat number already exists
            if any(ticket.seat_number == str(next_seat_number) for ticket in self.all_tickets):
                print(f"Seat Number {next_seat_number} already exists. Trying the next seat number...")
            else:
                return next_seat_number

    @classmethod
    def customer_id(cls):
        count = 0
        customerId = []
        while count <= 3:
            for i in range(0, 3):
                random_range = random.randrange(5)
                customerId.append(i + random_range)
            break
        random_num_gen = ''.join(str(item) for item in customerId)
        return random_num_gen

    @classmethod
    def booking_id(cls):
        bookingId = []
        booking_digit_count = 0
        while booking_digit_count <= 5:
            for i in range(0, 5):
                random_range = random.randrange(5)
                bookingId.append(i + random_range)
            break
        random_booking_gen = ''.join(str(item) for item in bookingId)
        return random_booking_gen

    def setup_style(self):
        """Set up modern ttk styles for the UI."""
        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Button style
        style.configure("TButton", font=("Helvetica", 12, 'bold'), padding=10,
                        relief="flat", background="#22f", foreground="white")
        style.map("TButton", background=[("active", "#55F"), ("pressed", "#33f")],
                  foreground=[("active", "white"), ("pressed", "white")])

        # Label style
        style.configure("TLabel", font=("Helvetica", 11), padding=5)

    def create_layout(self):
        """Create the main layout with left and right frames."""
        self.left_frame = tk.Frame(self.root, bg="white")
        self.left_frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        self.right_frame = tk.Frame(self.root, bg="white", relief="sunken", bd=1)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.display_area = tk.Frame(self.right_frame, bg="white")
        self.display_area.pack(fill="both", expand=True, padx=10, pady=10)

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

    def create_widgets(self):
        """Create widgets for the UI."""
        header_label = ttk.Label(
            self.left_frame,
            text="Welcome to Airlude Airline Ticket Reservation System",
            font=("Helvetica", 16, "bold"),
            anchor="center",
            background="white"
        )
        header_label.pack(pady=10)

        subheader_label = ttk.Label(
            self.left_frame,
            text="You are a ticket away from your destination!",
            font=("Helvetica", 12),
            anchor="center",
            background="white"
        )
        subheader_label.pack(pady=5)

        # Seat info labels
        self.available_seats_label = ttk.Label(self.left_frame, text="", background="black", foreground="white")
        self.available_seats_label.pack(pady=10)

        self.booked_seats_label = ttk.Label(self.left_frame, text="")
        self.booked_seats_label.pack(pady=10)

        # Menu Buttons
        buttons = [
            ("Book a Reservation", self.show_booking_form),
            ("Modify a Reservation", self.modify_reservation),
            ("Cancel a Reservation", self.cancel_reservation),
            ("View Reservation Details", self.view_reservation),
            ("View Seat Mapping", self.view_seat_mapping),
            ("Exit", self.exit_system),
        ]

        for text, command in buttons:
            btn = ttk.Button(self.left_frame, text=text, command=command)
            btn.pack(fill="x", pady=5)

    def update_seats_info(self):
        """Update seat information labels dynamically."""
        total_booked = self.count_booked_seats()
        self.available_seats_label.config(
            text=f"Total Seats Available: {self.total_seats - total_booked}"
        )
        self.booked_seats_label.config(
            text=f"Total Seats Booked: {total_booked}"
        )

    def count_booked_seats(self):
        """Count the total booked seats from Ticketing."""
        return len(self.ticket_manager.all_tickets)

    def clear_display_area(self):
        """Clear all widgets in the display area."""
        for widget in self.display_area.winfo_children():
            widget.destroy()

    def validate_name(self, name):
        """Validate a name based on specific rules."""
        name = name.strip().title()
        if len(name) < 3:
            return "Name must have at least 3 characters."
        elif any(char.isdigit() for char in name):
            return "Name cannot contain numbers."
        elif not all(char.isalpha() or char.isspace() for char in name):
            return "Name cannot contain symbols or special characters."
        return None  # No error means the name is valid



    def show_booking_form(self):
        self.clear_display_area()

        # First Name
        first_name_label = ttk.Label(self.display_area, text="First Name:")
        first_name_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.first_name_entry = ttk.Entry(self.display_area)
        self.first_name_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

        # Last Name
        last_name_label = ttk.Label(self.display_area, text="Last Name:")
        last_name_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.last_name_entry = ttk.Entry(self.display_area)
        self.last_name_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        # Submit Button
        submit_button = ttk.Button(self.display_area, text="Submit", command=self.book_reservation)
        submit_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")

        # Configure column weights for equal spacing
        self.display_area.grid_columnconfigure(0, weight=1)
        self.display_area.grid_columnconfigure(1, weight=1)

    def book_reservation(self):
        """Handle booking logic and display confirmation message."""
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()

        # Validate First Name
        first_name_error = self.validate_name(first_name)
        if first_name_error:
            self.show_message(f"First Name Error: {first_name_error}")
            return

        # Validate Last Name
        last_name_error = self.validate_name(last_name)
        if last_name_error:
            self.show_message(f"Last Name Error: {last_name_error}")
            return

        # Booking logic
        fullname = f"{first_name} {last_name}"
        ticket_number = f'{self.customer_id()}-{self.booking_id()}'
        seat_number = self.assign_seat_number()
        window_seat = str(seat_number % 2 == 0)  # For window seat validation
        booking_time = self.time
        status = 'Active'.title()

        my_ticket = self.config_ticket(self.customer_id(), fullname, ticket_number, seat_number, booking_time, status,
                                       window_seat)
        frontend_payload = my_ticket.prep_payload()

        # Construct the success message
        display_payload = f"Name: {frontend_payload['fullname']}\n" \
                          f"Ticket Number: {frontend_payload['ticket_number']}\n" \
                          f"Seat Number: {frontend_payload['seat_number']}\n" \
                          f"Window Seat: {frontend_payload['window_seat']}"

        seats_remaining = 100 - len([ticket for ticket in self.all_tickets if ticket.status == "Active"])

        # Confirmation message
        success_message = f"\nHello {first_name}!\n" \
                          f"Your flight ticket with the following details has been booked successfully!:\n" \
                          f"{display_payload}\n\n" \
                          f"Seats remaining: {seats_remaining}"

        # Append to the display area
        self.show_message(success_message)



    def modify_reservation(self):
        """Modify an existing reservation."""
        self.ticket_manager.edit_ticket()
        self.update_seats_info()

    def cancel_reservation(self):
        """Cancel a reservation."""
        self.ticket_manager.del_tickets()
        self.update_seats_info()

    def view_reservation(self):
        """View reservation details."""
        self.ticket_manager.read_tickets()

    def view_seat_mapping(self):
        """View seat mapping."""
        self.ticket_manager.print_window_seats()

    def show_message(self, message):
        """Display a message by replacing any existing message in the display area."""

        # Check if a message label already exists and remove it
        if hasattr(self, 'current_message_label') and self.current_message_label.winfo_exists():
            self.current_message_label.destroy()

        # Get the width of the display area for the wraplength (max width for wrapping)
        display_width = self.display_area.winfo_width()

        # Set a wraplength that is 80% of the display area's width (or a fixed value)
        wraplength = display_width * 0.8 if display_width > 0 else 500  # default wraplength if display_width is not yet available

        # Create the new message label with wrapping
        self.current_message_label = ttk.Label(self.display_area, text=message, font=("Helvetica", 12), wraplength=wraplength)
        self.current_message_label.grid(row=self.display_area.grid_size()[1], column=0, columnspan=2, sticky="w", pady=10, padx=10)

    def exit_system(self):
        """Exit the application."""
        self.root.quit()


# ========================= Initializer ==================
if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeGUI(root)
    root.mainloop()
