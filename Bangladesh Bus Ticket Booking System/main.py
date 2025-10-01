from admin import Admin
from system import BusSystem
from passenger import Passenger

admin = Admin("admin", "1234")
system = BusSystem(admin)

def admin_menu():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if not admin.login(username, password):
        print("Invalid credentials. Access denied.")
        return

    system.logged_in = True
    print("Welcome Admin", username)

    while system.logged_in:
        print("\nAdmin Menu:")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. View All Passengers")
        print("4. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            system.add_bus()
        elif choice == "2":
            system.view_all_buses()
        elif choice == "3":
            system.view_passengers()
        elif choice == "4":
            system.logged_in = False
            print("Admin logged out. Returning to Main Menu...")
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while True:
        print("\n===== User Menu =====")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            system.book_ticket()
        elif choice == "3":
            system.view_buses()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

user_menu()
