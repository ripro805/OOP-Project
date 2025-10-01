from bus import Bus
from passenger import Passenger

class BusSystem:
    def __init__(self, admin):
        self.admin = admin
        self.buses = []
        self.passengers = []
        self.logged_in = False

    def add_bus(self):
        if not self.logged_in:
            print("Access denied. Admin login required.")
            return

        number = input("Enter Bus Number: ")
        route = input("Enter Bus Route: ")
        seats = input("Enter Total Seats: ")

        if not seats.isdigit() or int(seats) <= 0:
            print("Invalid input. Total seats must be a positive number.")
            return

        bus = Bus(number, route, int(seats))
        self.buses.append(bus)
        print("Bus", number, "added successfully.")

    def view_all_buses(self):
        if not self.logged_in:
            print("Access denied. Admin login required.")
            return

        if len(self.buses) == 0:
            print("No buses in the system.")
            return

        print("\nAll Buses:")
        for bus in self.buses:
            print("Bus Number:", bus.number, "Route:", bus.route, "Available Seats:", bus.available_seats())

    def view_passengers(self):
        if not self.logged_in:
            print("Access denied. Admin login required.")
            return

        if len(self.passengers) == 0:
            print("No passengers have booked tickets yet.")
            return

        print("\nPassengers List:")
        for p in self.passengers:
            bus_info = p.bus.number + " (" + p.bus.route + ")" if p.bus else "No bus assigned"
            print("Name:", p.name, "Phone:", p.phone, "Bus:", bus_info, "Fare:", p.fare)

    def view_buses(self):
        if len(self.buses) == 0:
            print("No buses in the system.")
            return

        print("\nAvailable Buses:")
        for bus in self.buses:
            print("Bus Number:", bus.number, "Route:", bus.route, "Available Seats:", bus.available_seats())

    def book_ticket(self):
        if len(self.buses) == 0:
            print("No buses available for booking.")
            return

        bus_number = input("Enter Bus Number to book ticket: ")
        bus = None
        for b in self.buses:
            if b.number == bus_number:
                bus = b
                break

        if bus is None:
            print("Bus not found.")
            return

        if bus.available_seats() == 0:
            print("No seats available on this bus.")
            return

        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        passenger = Passenger(name, phone, bus)
        bus.book_seat()
        self.passengers.append(passenger)
        print("Ticket booked for", name, "on bus", bus.number, "Fare:", passenger.fare)
