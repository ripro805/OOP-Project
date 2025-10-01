from marketplace import Marketplace

marketplace = Marketplace()

# ------------------- Customer Menu -------------------
def customer_menu():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    customer = marketplace.register_customer(email, password)

    while True:
        print(f"\n===== Customer Menu ({customer.email}) =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer.view_products(marketplace)
        elif choice == "2":
            product_id = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))
            customer.add_to_cart(marketplace, product_id, qty)
        elif choice == "3":
            customer.view_cart()
        elif choice == "4":
            customer.checkout()
        elif choice == "5":
            print("Exiting Customer Menu...")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------- Seller Menu -------------------
def seller_menu():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    seller = marketplace.register_seller(email, password)

    while True:
        print(f"\n===== Seller Menu ({seller.email}) =====")
        print("1. Add Product")
        print("2. View My Products")
        print("3. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            seller.add_product(marketplace, name, price, stock)
        elif choice == "2":
            print("\n===== My Products =====")
            if not seller.products:
                print("No products added yet.")
            else:
                for p in seller.products:
                    print(f"ID: {p.id} | {p.name} | Price: {p.price} | Stock: {p.stock}")
        elif choice == "3":
            print("Exiting Seller Menu...")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------- Main Menu -------------------
while True:
    print("\n===== E-Shopping Main Menu =====")
    print("1. Customer")
    print("2. Seller")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        customer_menu()
    elif choice == "2":
        seller_menu()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
