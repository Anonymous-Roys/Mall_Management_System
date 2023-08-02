class Cart:
    # Constructor to initialize the cart with empty items
    def __init__(self):
        self.items = {}

    # Method to add items to the cart
    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
        print(f"Added {quantity} {product.name}(s) to the cart. Total cost: ${product.price * quantity:.2f}")

    # Method to remove items from the cart
    def remove_item(self, product, quantity):
        if product in self.items:
            if self.items[product] >= quantity:
                self.items[product] -= quantity
                print(f"Removed {quantity} {product.name}(s) from the cart.")
                if self.items[product] == 0:
                    del self.items[product]
            else:
                print(f"Error: There are only {self.items[product]} {product.name}(s) in the cart.")
        else:
            print(f"Error: {product.name} is not in the cart.")

    # Method to view the cart contents
    def view_cart(self):
        print("\nCart contents:")
        for product, quantity in self.items.items():
            print(f"{product.name} - Quantity: {quantity} - Price: ${product.price * quantity:.2f}")
