from menuitem import MenuItem
from menu import Menu 
from restaurant import Restaurant
from user import Customer, Employee, Admin
from orders import Order

restaurant = Restaurant("Fresh Cake by Prova")

# ------------------- Customer Menu -------------------
def customer_menu(customer, restaurant):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f"\nWelcome {customer.name} to {restaurant.name}!!")
        print("\n===== Customer Menu =====")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Checkout")   
        print("5. Exit")
         
        choice = input("Enter your choice: ")
        if choice == "1":
            customer.view_menu(restaurant)
        elif choice == "2":
            item_name = input("Enter item name to add to cart: ")
            quantity = int(input("Enter quantity: "))
            customer.add_to_cart(restaurant, item_name, quantity) 
        elif choice == "3":
            customer.view_cart()
        elif choice == "4":
            customer.cart.checkout()
        elif choice == "5":
            print("Exiting customer menu. Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")             
             

# ------------------- Admin Menu -------------------
def admin_menu(customer, restaurant):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f"\nWelcome {admin.name}!!")
        print("\n===== Admin Menu =====")
        print("1. Add New Item to Menu")
        print("2. Add New Employee")
        print("3. View Employees")
        print("4. View Items in Menu")
        print("5. Remove Item from Menu")   
        print("6. Exit")
         
        choice = input("Enter your choice: ")
        if choice == "1":
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = MenuItem(item_name, item_price, item_quantity)
            admin.add_menu_item(restaurant, item)
        elif choice == "2":
            emp_name = input("Enter employee name: ")
            emp_email = input("Enter employee email: ")
            emp_phone = input("Enter employee phone: ")
            emp_address = input("Enter employee address: ")
            emp_age = int(input("Enter employee age: "))
            emp_designation = input("Enter employee designation: ")
            emp_salary = float(input("Enter employee salary: "))
            employee = Employee(
                name=emp_name, email=emp_email, phone=emp_phone,
                address=emp_address, age=emp_age,
                designation=emp_designation, salary=emp_salary
            )
            admin.add_employee(restaurant, employee)
        elif choice == "3":
            admin.view_employees(restaurant)
        elif choice == "4":
            restaurant.menu.show_menu()
        elif choice == "5":
            item_name = input("Enter item name to remove from menu: ")
            admin.remove_menu_item(restaurant, item_name)   
        elif choice == "6":
            print("Exiting admin menu. Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")                                


# ------------------- Main Menu -------------------
while True:
    print("\n===== Main Menu =====")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        customer_menu(Customer, restaurant)
    elif choice == "2":
        admin_menu(Admin, restaurant)
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
