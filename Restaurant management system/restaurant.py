from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()
     
    def add_employee(self, employee):
        self.employees.append(employee)   
  
    def view_employees(self):
        print("\n===== Employee List =====")
        if not self.employees:
            print("No employees available.")
        else:
            for emp in self.employees:
                print(f"Name: {emp.name}, Email: {emp.email}, Phone: {emp.phone}, "
                      f"Address: {emp.address}, Age: {emp.age}, "
                      f"Designation: {emp.designation}, Salary: {emp.salary}")
