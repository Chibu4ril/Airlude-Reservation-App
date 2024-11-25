import csv
import tkinter as tk
from tkinter import ttk
from bookinggui import Ticketing
from datetime import datetime
from ticketconfig import TicketConfig
from ticketconfig import CancelledTicketConfig
import random

TICKETS_FILE = 'gui_flight_db.csv'
CANCELLED_TICKETS_FILE = 'deleted_gui_flight_db.csv'

class WelcomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="white")
        self.root.title("Airlude Airline Ticket Reservation System")
        self.root.geometry("1000x550")
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.all_tickets = self.query_tickets()
        self.config_ticket = TicketConfig
        self.customer_id = self.customer_id()
        self.all_cancelled_tickets = []

        # Ticketing logic
        self.ticket_manager = Ticketing()
        self.total_seats = 100

        # Initialize UI
        self.setup_style()
        self.create_layout()
        self.create_widgets()
        self.update_seats_info()


    def write_to_csv(self):
        with open(TICKETS_FILE, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat'])
            writer.writeheader()
            for ticket in self.all_tickets:
                writer.writerow(ticket.prep_payload())
            record.flush()
        self.all_tickets = self.query_tickets()


    def write_to_cancelled_csv(self):
        if not hasattr(self, 'all_cancelled_tickets'):
            self.all_cancelled_tickets = []

        with open(CANCELLED_TICKETS_FILE, mode='w', newline='') as record:
            writer = csv.DictWriter(record, fieldnames=['customer_id', 'fullname', 'ticket_number', 'seat_number', 'booking_time', 'status', 'window_seat', 'cancelled_date'])
            writer.writeheader()
            for ticket in self.all_cancelled_tickets:
                if isinstance(ticket, CancelledTicketConfig):  # Ensure correct type
                    writer.writerow(ticket.cancelled_ticket_payload())
                else:
                    print(f"Skipped invalid object in cancelled tickets: {ticket}")

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

        default_text = ["CSC-40044 System Design & Programming", "Course Work", "By Innocent Onyenonachi"]
        for i, text in enumerate(default_text):
            label = tk.Label(self.display_area, text=text, font=("Arial", 12), bg="white", anchor="center")
            label.grid(row=i, column=0, padx=20, pady=2, sticky="ew")

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
            ("View Reservation Details", self.view_reservation),
            ("Modify a Reservation", self.modify_reservation),
            ("Cancel a Reservation", self.cancel_reservation),
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

        details_label = ttk.Label(self.display_area, text="Book a Ticket",
                                  font=("Helvetica", 14, "bold"), background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        # First Name
        first_name_label = ttk.Label(self.display_area, text="First Name:")
        first_name_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.first_name_entry = ttk.Entry(self.display_area)
        self.first_name_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        # Last Name
        last_name_label = ttk.Label(self.display_area, text="Last Name:")
        last_name_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.last_name_entry = ttk.Entry(self.display_area)
        self.last_name_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        # Submit Button
        submit_button = ttk.Button(self.display_area, text="Submit", command=self.book_reservation)
        submit_button.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")

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
        fullname = f"{first_name.title()} {last_name.title()}"
        ticket_number = f'{self.customer_id}-{self.booking_id()}'
        seat_number = self.assign_seat_number()

        def window_seat_checker(seat_number):
            # Check if a given seat number is a window seat.
            if (seat_number - 1) % 3 == 0:
                return "This is a Window seat"
            else:
                return "Not a Window Seat"

        window_seat = window_seat_checker(seat_number)
        booking_time = self.time
        status = 'Active'.title()

        my_ticket = self.config_ticket(self.customer_id, fullname, ticket_number, seat_number, booking_time, status,
                                       window_seat)
        frontend_payload = my_ticket.prep_payload()

        self.all_tickets.append(my_ticket)
        self.write_to_csv()

        self.clear_input_fields()

        # Construct the success message
        display_payload = f"Name: {frontend_payload['fullname']}\n" \
                          f"Ticket Number: {frontend_payload['ticket_number']}\n" \
                          f"Customer ID: {frontend_payload['customer_id']}\n" \
                          f"Seat Number: {frontend_payload['seat_number']}\n" \
                          f"Window Seat: {frontend_payload['window_seat']}"

        seats_remaining = 100 - len([ticket for ticket in self.all_tickets if ticket.status == "Active"])

        # Confirmation message
        success_message = f"Hello {first_name.upper()}!\n\n" \
                          f"Your flight ticket with the following details has been booked successfully!\n\n" \
                          f"{display_payload}\n" \
                          f"\nSEATS REMAINING: {seats_remaining} seats available"\

        # Append to the display area
        self.show_message(success_message)



    def clear_input_fields(self):
        """Clear the input fields in the booking form."""
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)

    # =================Edit Ticket=====================================
    def modify_reservation(self):
        """Modify an existing reservation."""
        self.clear_display_area()

        details_label = ttk.Label(self.display_area, text="Edit Ticket",
                                  font=("Helvetica", 14, "bold"), background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=15, sticky="w")


        # Ticket Number Input
        ticket_number_label = ttk.Label(self.display_area, text="Enter Ticket Number:")
        ticket_number_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.ticket_number_entry = ttk.Entry(self.display_area)
        self.ticket_number_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        # Submit Button
        submit_button = ttk.Button(self.display_area, text="Search", command=self.search_ticket)
        submit_button.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")

        # Configure column weights for equal spacing
        self.display_area.grid_columnconfigure(0, weight=1)
        self.display_area.grid_columnconfigure(1, weight=1)

    def search_ticket(self):
        """Search for a ticket by ticket number and allow modification."""
        ticket_number = self.ticket_number_entry.get().strip()

        # Search for the ticket
        ticket_found = None
        for row in self.all_tickets:
            if row.ticket_number == ticket_number:
                ticket_found = row
                break

        if not ticket_found:
            self.show_message(f"No ticket found with Ticket Number: {ticket_number}")
            return

        # Display current ticket details and input fields for modification
        self.display_edit_form(ticket_found)

    def display_edit_form(self, ticket):
        """Display the ticket's current details and fields for modification."""
        self.clear_display_area()

        details_label = ttk.Label(self.display_area, text="Edit Ticket",
                                  font=("Helvetica", 12, "bold"), background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        # Display Current Details
        details_label = ttk.Label(self.display_area, text="Current Reservation Details:",
                                  font=("Helvetica", 12, "bold"), background='white')
        details_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

        fields = {
            "Name": ticket.fullname,
            "Ticket Number": ticket.ticket_number,
            "Seat Number": ticket.seat_number,
            "Status": ticket.status,
            "Booking Time": ticket.booking_time,
        }

        for i, (key, value) in enumerate(fields.items(), start=2):
            label = ttk.Label(self.display_area, text=f"{key}: {value}", background='white')
            label.grid(row=i, column=0, columnspan=2, pady=5, sticky="w")

        # Display Modifying Contents
        details_label = ttk.Label(self.display_area, text="Enter New Details", font=("Helvetica", 12, "bold"), background='white')
        details_label.grid(row=len(fields) + 3, column=0, columnspan=2, pady=5, sticky="w")

        # Input for New First Name
        first_name_label = ttk.Label(self.display_area, text="New First Name:")
        first_name_label.grid(row=len(fields) + 4, column=0, pady=5, sticky="w")
        self.first_name_entry = ttk.Entry(self.display_area)
        self.first_name_entry.insert(0, ticket.fullname.split(" ")[0])  # Prefill current first name
        self.first_name_entry.grid(row=len(fields) + 4, column=1, pady=5, sticky="ew")

        # Input for New Last Name
        last_name_label = ttk.Label(self.display_area, text="New Last Name:")
        last_name_label.grid(row=len(fields) + 5, column=0, pady=5, sticky="w")
        self.last_name_entry = ttk.Entry(self.display_area)
        self.last_name_entry.insert(0, ticket.fullname.split(" ")[1])  # Prefill current last name
        self.last_name_entry.grid(row=len(fields) + 5, column=1, pady=5, sticky="ew")

        # Save Button
        save_button = ttk.Button(self.display_area, text="Save Changes", command=lambda: self.save_changes(ticket))
        save_button.grid(row=len(fields) + 6, column=0, columnspan=2, pady=20, sticky="ew")

        # Configure column weights
        self.display_area.grid_columnconfigure(0, weight=1)
        self.display_area.grid_columnconfigure(1, weight=1)

    def save_changes(self, ticket):
        """Save the updated details for the ticket."""
        new_first_name = self.first_name_entry.get().strip().title() or ticket.fullname.split(" ")[0]
        new_last_name = self.last_name_entry.get().strip().title() or ticket.fullname.split(" ")[1]
        ticket.fullname = f"{new_first_name} {new_last_name}"

        # Update the tickets file
        self.write_to_csv()

        self.clear_display_area()

        # Display confirmation heading
        confirmation_label = ttk.Label(
            self.display_area,
            text="Reservation Updated Successfully!",
            font=("Helvetica", 14, "bold"),
            foreground="green",
            background='white'
        )
        confirmation_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        # Display updated details heading
        details_label = ttk.Label(
            self.display_area,
            text="Updated Reservation Details:",
            font=("Helvetica", 12, "bold"),
            background="white"
        )
        details_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

        # Updated details fields
        fields = {
            "Name": ticket.fullname,
            "Ticket Number": ticket.ticket_number,
            "Seat Number": ticket.seat_number,
            "Status": ticket.status,
            "Booking Time": ticket.booking_time,
        }

        # Dynamically display fields
        for idx, (label, value) in enumerate(fields.items(), start=2):
            field_label = ttk.Label(self.display_area, text=f"{label}:", font=("Helvetica", 10, "bold"), background='white')
            field_label.grid(row=idx, column=0, pady=5, padx=10, sticky="w")

            field_value = ttk.Label(self.display_area, text=value, font=("Helvetica", 10), background='white')
            field_value.grid(row=idx, column=1, pady=5, padx=10, sticky="w")

    def search_reserved_ticket(self):
        """Search for a ticket by ticket number and allow modification."""
        ticket_number = self.ticket_number_entry.get().strip()

        # Search for the ticket
        ticket_found = None
        for row in self.all_tickets:
            if row.ticket_number == ticket_number:
                ticket_found = row
                break

        if not ticket_found:
            self.show_message(f"No ticket found with Ticket Number: {ticket_number}")
            return

        # Display current ticket details and input fields for modification
        self.display_details(ticket_found)

    def display_details(self, ticket):
        self.clear_display_area()

        details_label = ttk.Label(self.display_area, text="View Reserved Ticket",
                                  font=("Helvetica", 14, "bold"), background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        # Display Current Details
        details_label = ttk.Label(self.display_area, text="Current Reservation Details:",
                                  font=("Helvetica", 12, "bold"), background='white')
        details_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

        fields = {
            "Name": ticket.fullname,
            "Ticket Number": ticket.ticket_number,
            "Seat Number": ticket.seat_number,
            "Status": ticket.status,
            "Booking Time": ticket.booking_time,
        }

        for i, (key, value) in enumerate(fields.items(), start=2):
            label = ttk.Label(self.display_area, text=f"{key}: {value}", background='white')
            label.grid(row=i, column=0, columnspan=2, pady=5, sticky="w")





    def view_reservation(self):
        """View reservation details."""
        self.clear_display_area()

        details_label = ttk.Label(self.display_area, text="View Reserved Ticket Details",
                                  font=("Helvetica", 14, "bold"), background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        # Ticket Number Input
        ticket_number_label = ttk.Label(self.display_area, text="Enter Ticket Number:")
        ticket_number_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.ticket_number_entry = ttk.Entry(self.display_area)
        self.ticket_number_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        # Submit Button
        submit_button = ttk.Button(self.display_area, text="Search", command=self.search_reserved_ticket)
        submit_button.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")

        # Configure column weights for equal spacing
        self.display_area.grid_columnconfigure(0, weight=1)
        self.display_area.grid_columnconfigure(1, weight=1)

    def display_reservation(self, ticket):
        self.clear_display_area()
        # Display Current Details
        details_label = ttk.Label(self.display_area, text="Current Reservation Details:",
                                  font=("Helvetica", 12, "bold"), background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        fields = {
            "Name": ticket.fullname,
            "Ticket Number": ticket.ticket_number,
            "Seat Number": ticket.seat_number,
            "Status": ticket.status,
            "Booking Time": ticket.booking_time,
        }

        for i, (key, value) in enumerate(fields.items(), start=1):
            label = ttk.Label(self.display_area, text=f"{key}: {value}", background='white')
            label.grid(row=i, column=0, columnspan=2, pady=5, sticky="w")

    def cancel_reservation(self):
        """Cancel a reservation."""
        self.clear_display_area()
        # Display Current Details
        details_label = ttk.Label(self.display_area, text="Cancel a Reservation",
                                  font=("Helvetica", 12, "bold"), background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        # Ticket Number Input
        ticket_number_label = ttk.Label(self.display_area, text="Enter Ticket Number:")
        ticket_number_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.ticket_number_entry = ttk.Entry(self.display_area)
        self.ticket_number_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        # Submit Button
        submit_button = ttk.Button(self.display_area, text="Search", command=self.search_ticket_to_delete)
        submit_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")

        # Configure column weights for equal spacing
        self.display_area.grid_columnconfigure(0, weight=1)
        self.display_area.grid_columnconfigure(1, weight=1)

    def search_ticket_to_delete(self):
        """Search for a ticket by ticket number and allow modification."""
        ticket_number = self.ticket_number_entry.get().strip()

        # Search for the ticket
        ticket_found = None
        for row in self.all_tickets:
            if row.ticket_number == ticket_number:
                ticket_found = row
                break

        if not ticket_found:
            self.show_message(f"No ticket found with Ticket Number: {ticket_number}")
            return

        # Display current ticket details and input fields for modification
        self.display_delete_confirm(ticket_found)

    def display_delete_confirm(self, ticket):
        """Display the ticket's current details and fields for modification."""
        self.clear_display_area()

        details_label = ttk.Label(self.display_area, text="Delete Ticket", font=("Helvetica", 14, "bold"),
                                  background='white')
        details_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        # Display Current Details
        current_details_label = ttk.Label(self.display_area, text="Current Reservation Details:",
                                          font=("Helvetica", 12, "bold"), background='white')
        current_details_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

        fields = {
            "Name": ticket.fullname,
            "Ticket Number": ticket.ticket_number,
            "Seat Number": ticket.seat_number,
            "Status": ticket.status,
            "Booking Time": ticket.booking_time,
        }

        for i, (key, value) in enumerate(fields.items(), start=2):
            label = ttk.Label(self.display_area, text=f"{key}: {value}", background='white')
            label.grid(row=i, column=0, columnspan=2, pady=5, sticky="w")

        # Confirmation Question
        confirmation_qst = ttk.Label(self.display_area, text="Are you Sure You Want to Cancel?",
                                     font=("Helvetica", 14, "bold"), background='white')
        confirmation_qst.grid(row=len(fields) + 2, column=0, columnspan=2, pady=5, sticky="w")

        confirmation_label = ttk.Label(self.display_area, text="Type YES to confirm cancellation:")
        confirmation_label.grid(row=len(fields) + 3, column=0, pady=5, sticky="w")
        self.confirmation_entry = ttk.Entry(self.display_area)
        self.confirmation_entry.grid(row=len(fields) + 4, column=0, columnspan=2, pady=5, sticky="ew")

        # Cancel Button
        cancel_button = ttk.Button(self.display_area, text="Proceed With Delete",
                                   command=lambda: self.delete_changes(ticket))
        cancel_button.grid(row=len(fields) + 5, column=0, columnspan=2, pady=20, sticky="ew")

        # Configure column weights
        self.display_area.grid_columnconfigure(0, weight=1)
        self.display_area.grid_columnconfigure(1, weight=1)

    def delete_changes(self, ticket):
        """Handle the deletion of a ticket."""
        confirmation = self.confirmation_entry.get().strip().upper()

        if confirmation != "YES":
            self.show_message("Cancellation aborted. Please type 'YES' to confirm cancellation.")
            return

        # Remove the ticket from the list
        self.all_tickets = [t for t in self.all_tickets if t.ticket_number != ticket.ticket_number]

        # Update the CSV file
        self.write_to_csv()

        # Clear the display area
        self.clear_display_area()

        # Display confirmation message
        confirmation_label = ttk.Label(
            self.display_area,
            text="Reservation Cancelled Successfully!",
            font=("Helvetica", 14, "bold"),
            foreground="red",
            background='white'
        )
        confirmation_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        # Show canceled ticket details
        details_label = ttk.Label(
            self.display_area,
            text="Cancelled Reservation Details:",
            font=("Helvetica", 12, "bold"),
            background="white"
        )
        details_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

        fields = {
            "Name": ticket.fullname,
            "Ticket Number": ticket.ticket_number,
            "Seat Number": ticket.seat_number,
            "Status": "Cancelled",
            "Booking Time": ticket.booking_time,
        }

        for idx, (label, value) in enumerate(fields.items(), start=2):
            field_label = ttk.Label(self.display_area, text=f"{label}:", font=("Helvetica", 10, "bold"), background="white")
            field_label.grid(row=idx, column=0, pady=5, padx=10, sticky="w")

            field_value = ttk.Label(self.display_area, text=value, font=("Helvetica", 10))
            field_value.grid(row=idx, column=1, pady=5, padx=10, sticky="w")

        # Provide seat update info
        self.update_seats_info()

    def view_seat_mapping(self, total_seats=101, seats_per_row=3):
        """Display the seating chart in the Tkinter interface."""
        self.clear_display_area()

        # Title
        title_label = ttk.Label(self.display_area, text="Seat Reservation Mapping", font=("Helvetica", 10, "bold"), background='white')
        title_label.grid(row=0, column=0, columnspan=seats_per_row, pady=10, sticky="ew")

        booked_seats = [int(ticket.seat_number) for ticket in self.all_tickets if ticket.status == 'Active']

        seat_number = 1
        row_index = 1

        for row in range(1, (total_seats // seats_per_row) + 2):
            for seat in range(seats_per_row):
                if seat_number >= total_seats:
                    break

                # Determine if the seat is a window seat (every third seat starting from 1)
                is_window_seat = seat_number % seats_per_row == 1

                # Check if the seat is booked
                if seat_number in booked_seats:
                    seat_label = tk.Label(self.display_area, text=" X ",
                                          background="red", foreground="white",
                                          font=("Helvetica", 10, "bold"), borderwidth=1, relief="solid")
                else:
                    if is_window_seat:
                        seat_label = tk.Label(self.display_area, text=f"{seat_number:2}",
                                              background="blue", foreground="white",
                                              font=("Helvetica", 10, "bold"), borderwidth=1, relief="solid")
                    else:
                        seat_label = tk.Label(self.display_area, text=f"{seat_number:2}",
                                              background="green", foreground="white",
                                              font=("Helvetica", 10, "bold"), borderwidth=1, relief="solid")

                seat_label.grid(row=row_index, column=seat, padx=2, pady=2, sticky="nsew")

                seat_number += 1

            row_index += 1

        # Adjust the grid to scale with the display area
        for col in range(seats_per_row):
            self.display_area.grid_columnconfigure(col, weight=1)

        # Configure rows to use space efficiently
        self.display_area.grid_rowconfigure(0, weight=0)
        for row in range(1, row_index):
            self.display_area.grid_rowconfigure(row, weight=1)



    def show_message(self, message):
        # Check if a message label already exists and remove it
        if hasattr(self, 'current_message_label') and self.current_message_label.winfo_exists():
            self.current_message_label.destroy()

        display_width = self.display_area.winfo_width()

        wraplength = display_width * 0.85 if display_width > 0 else 600

        # Create the new message label with wrapping
        self.current_message_label = ttk.Label(self.display_area, text=message, font=("Helvetica", 12), wraplength=wraplength, background='white')
        self.current_message_label.grid(row=self.display_area.grid_size()[1], column=0, columnspan=2, sticky="w", pady=10, padx=10)

    def exit_system(self):
        """Exit the application."""
        self.root.quit()


# ========================= Initializer ==================
if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeGUI(root)
    root.mainloop()
