import json
import os

# Inventory Management System
class Inventory:
    total_items = 0 

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price 
        self.quantity = quantity
        Inventory.total_items += quantity

    # Instance Method : Show product details
    def show_product_details(self):    
        print("\n---Product Details---")
        print(f"Product name : {self.product_name}")
        print(f"Price : {self.price}")
        print(f"Quantity : {self.quantity}")

    # Instance Method : Sell Product
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount
            print(f"{amount} {self.product_name}(s) sold!")
        else:
            print("Insufficient quantity.") 

    # Static Method: Calculate Discount 
    @staticmethod 
    def calculate_discount(price, discount_percentage):
        return price * (1 - discount_percentage/100)

    # Class Method: Total Items Report
    @classmethod  
    def total_items_report(cls):
        print(f"\nTotal Items: {cls.total_items}")

    # Convert object → dictionary (for JSON)
    def to_dict(self):
        return {
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity
        }

    # Create object from dictionary (for JSON)
    @classmethod
    def from_dict(cls, data):
        return cls(data["product_name"], data["price"], data["quantity"])


# JSON Handling
FILENAME = "inventory.json"

def save_inventory():
    with open(FILENAME, "w") as file:
        json.dump([product.to_dict() for product in products], file, indent=4)

def load_inventory():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        data = json.load(file)
        return [Inventory.from_dict(item) for item in data]


# Main Program
products = load_inventory()  # Load saved inventory

# Recalculate total_items when loading
Inventory.total_items = sum(product.quantity for product in products)

# Add Product To Inventory
def add_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    product = Inventory(product_name, price, quantity)
    products.append(product)
    save_inventory()
    print(f"{quantity} {product_name}(s) added to inventory.")

# Display All Products
def view_products():
    print("\n---Inventory---")
    if not products:
        print("No products in inventory.")
    for product in products:
        product.show_product_details()    

# Sell Products
def sell_products():
    product_name = input("Enter product name to sell: ")
    for product in products:
        if product.product_name == product_name:
            amount = int(input("Enter the amount to sell: "))
            product.sell_product(amount)
            save_inventory()
            return
    print("Product not found in inventory.")        

# Calculate Discount
def discount_price():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount percentage: "))
    discounted_price = Inventory.calculate_discount(price, discount_percentage)
    print(f"Discounted Price: {discounted_price}")

# Main Menu
while True:
    print("\n---Inventory Management System---")
    print("1. Add Product")
    print("2. View products")
    print("3. Sell Products")
    print("4. Calculate Discount")
    print("5. Total items Report")
    print("6. Exit")                

    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        sell_products() 
    elif choice == "4":
        discount_price()
    elif choice == "5":
        Inventory.total_items_report()
    elif choice == "6":
        save_inventory()
        print("Exiting the program. Thank you!")     
        break              
    else:
        print("Invalid choice.") 
