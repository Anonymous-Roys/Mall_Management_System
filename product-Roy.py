# Defining the Product class
class Product:
    # Constructor to initialize the product with name, price, and manufacturing date
    def __init__(self, name, price, manufacturing_date):
        self.name = name
        self.price = price
        self.manufacturing_date = manufacturing_date

    # Method to display products
    def display_products(self):
        print("\nAvailable Products:")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product}")

    # Method to provide a string representation of the product
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - {self.manufacturing_date}"