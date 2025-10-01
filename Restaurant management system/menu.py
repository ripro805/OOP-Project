class Menu:
    def __init__(self):
        self.items = []  # List to store menu items

    def add_item(self,item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"Item '{item_name}' removed from the menu.")
        else:
            print(f"Item '{item_name}' not found in the menu.") 
            
    def show_menu(self):
        print("\n===== Menu =====")
        print("Name\tPrice\tQuantity")
        if not self.items:
            print("No items available in the menu.")
        else:
            for item in self.items:
                print(f"{item.name}\t{item.price}\t{item.quantity}")  
                