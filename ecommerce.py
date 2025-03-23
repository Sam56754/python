class Ecommerce:
    def __init__(self):
        self.products = []  # List to store multiple products

    def database(self):
        return self.products  # Returns all products
        
    def add_product(self):
        product = {
            "product_name": input("Enter product name: "),
            "price": self.get_valid_float("Enter the price: "),
            "quantity": self.get_valid_int("Enter the quantity: ")
        }
        
        self.products.append(product)
        print("Product added successfully!")
        return product

    def update_price(self):
        if not self.products:
            print("No products available to update.")
            return

        name = input("Enter product name to update price: ")
        for product in self.products:
            if product["product_name"].lower() == name.lower():
                product["price"] = self.get_valid_float("Enter new price: ")
                print("Product price updated successfully!")
                return product
        
        print("Product not found.")
    
    def update_quantity(self):
        if not self.products:
            print("No products available to update.")
            return

        name = input("Enter product name to update quantity: ")
        for product in self.products:
            if product["product_name"].lower() == name.lower():
                product["quantity"] = self.get_valid_int("Enter new quantity: ")
                print("Product quantity updated successfully!")
                return product
        
        print("Product not found.")

    @staticmethod
    def get_valid_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    @staticmethod
    def get_valid_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

# Create an instance of Ecommerce
money = Ecommerce()

# Menu Loop
while True:
    print("\n1. View database\n2. Add product\n3. Update price\n4. Update quantity\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        database = money.database()
        if database:
            print("Current Products:", database)
        else:
            print("No products available.")
    elif choice == "2":
        money.add_product()
    elif choice == "3":
        money.update_price()
    elif choice == "4":
        money.update_quantity()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
