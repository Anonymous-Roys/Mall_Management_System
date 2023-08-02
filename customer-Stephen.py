# Defining the Customer class
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.purchases = []

    # Method to top up the customer's balance
    def top_up_balance(self):
        while True:
            try:
                top_up_amount = float(input("Enter the amount to top up your balance: "))
                if top_up_amount > 0:
                    self.balance += top_up_amount
                    print(f"Your balance has been topped up. Your current balance: ${self.balance:.2f}")
                    break
                else:
                    print("Amount must be greater than 0. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    # Method to handle the customer's purchase
    def purchase(self, cart):
        total_cost = 0
        for product, quantity in cart.items.items():
            total_cost += product.price * quantity

        if total_cost > self.balance:
            print("Insufficient balance to complete the purchase.")
            self.top_up_balance()
            return

        print("\nCart contents:")
        for product, quantity in cart.items.items():
            print(f"{product.name} - Quantity: {quantity} - Price: ${product.price * quantity:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

        while True:
            try:
                confirmation = input("Confirm purchase (yes/no): ").strip().lower()
                if confirmation == "yes":
                    self.balance -= total_cost
                    self.purchases.append((datetime.datetime.now(), cart.items.copy()))
                    cart.items.clear()
                    print("Purchase successful!")
                    break
                elif confirmation == "no":
                    print("Purchase canceled.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            except ValueError:
                print("Invalid input. Please enter 'yes' or 'no'.")

    # Method to view the customer's purchases
    def view_purchases(self):
        print("\nYour purchases:")
        for timestamp, items in self.purchases:
            print(f"Date: {timestamp}")
            for product, quantity in items.items():
                print(f"{product.name} - Quantity: {quantity} - Price: ${product.price * quantity:.2f}")
