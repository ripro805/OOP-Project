# customer
# admin
# employee
from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)   # ✅ এখানে ঠিক করা হলো
        self.cart = Order()
        
    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
        
    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if item.quantity < quantity:
                print(f"Only {item.quantity} of '{item_name}' available in the menu.")
            else:     
                item.quantity = quantity  # Set the desired quantity
                self.cart.add_item(item)
                print(f"Added {quantity} of '{item_name}' to the cart.")
        else:
            print(f"Item '{item_name}' not found in the menu.") 
            
    def view_cart(self):
        print("\n===== Cart =====")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
                
        print(f"Total Price: {self.cart.total_price}")    

    def checkout(self):
        if not self.cart.items:
            print("Your cart is empty. Add items to the cart before checkout.")
        else:    
            print(f"Total amount to be paid: {self.cart.total_price}")
            print("Checkout successful. Thank you for your purchase!")
            self.cart.clear_cart()  # Clear the cart after checkout
 


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)   # ✅ ঠিক করা হলো
        self.age = age
        self.designation = designation
        self.salary = salary
      


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address) 
        
        
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
        
        
    def view_employees(self, restaurant):
        restaurant.view_employees()
        
    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_item(item)
        
    def remove_menu_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)
