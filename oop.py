import datetime   # Importing the datetime module for date manipulation


# Function to get the user's choice of product to add to the cart
def get_product_choice():
    while True:
        try:
            choice = int(input("Enter the product number to add to cart (0 to exit): "))
            if 0 <= choice <= len(products):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the quantity of the product to add to the cart
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the customer's balance
def get_balance():
    while True:
        try:
            balance = float(input("Please enter your balance: "))
            return balance
        except ValueError:
            print("Invalid input. Please enter a valid balance.")

# Create instances of the products with fixed prices
products = [
    Product("Laptop", 1200, datetime.date(2022, 1, 1)),
    Product("Mobile Phone", 600, datetime.date(2023, 5, 15)),
    Product("Charger", 20, datetime.date(2023, 3, 10))
]

# Main function to run the program
def main():
    print("Welcome to the Online Store!")
    name = input("Please enter your name: ")
    balance = get_balance()

    customer = Customer(name, balance)
    cart = Cart()

    while True:
        Product.display_products(products)
        choice = get_product_choice()

        if choice == 0:
            break

        product = products[choice - 1]
        quantity = get_quantity()

        cart.add_item(product, quantity)
        cart.view_cart()

    while True:
        print("")
        print("\nWhat would you like to do?")
        print("1. Remove items from the cart")
        print("2. Purchase items")
        print("3. View purchases")
        print("4. Add more items to cart")
        print("5. Exit")

        action = input("Enter the number corresponding to your choice: ")

        if action == "1":
            Product.display_products(products)
            choice = get_product_choice()

            if choice == 0:
                continue

            product = products[choice - 1]
            quantity = get_quantity()

            cart.remove_item(product, quantity)
            cart.view_cart()

        elif action == "2":
            customer.purchase(cart)

        elif action == "3":
            customer.view_purchases()

        elif action == "4":
            while True:
                Product.display_products(products)
                choice = get_product_choice()

                if choice == 0:
                    break

                product = products[choice - 1]
                quantity = get_quantity()

                cart.add_item(product, quantity)
                cart.view_cart()

        elif action == "5":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
