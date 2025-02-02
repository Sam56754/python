#inventory system program
inventory = {}

def view_inventory():
    for item, quantity in inventory.items():
        print(item, quantity)

def add_item():
    while True:
        item = input("Enter item name (or type 'exit' to go back): ").strip()
        if item.lower() == "exit":
            break  #back to the main menu

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity, Please enter a number.")
            continue  # edge case fpr quantity
        if quantity <1:
            print("invalid number")
            break
        else:
            if item in inventory:
                inventory[item] += quantity  # Update existing
            else:
                inventory[item] = quantity  # Add new
            print(f"{quantity} {item}(s) added successfully!")

def get_item():
    item = input("Enter item name to check: ").strip()
    
    if item in inventory:
        print(f"{item}: {inventory[item]} in stock")
    else:
        print(f"{item} is not in the inventory.")

def total_items():
    total = sum(inventory.values())
    print(f"Total number of items in inventory: {total}")

# Main program
while True:
    print("\n1. Add Item")
    print("2. Check Item Quantity")
    print("3. Show Total Inventory")
    print("4. View inventory")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        get_item()
    elif choice == "3":
        total_items()
    elif choice == "4":
        view_inventory()
    elif choice == "5":
        print("Exiting program...")
        break  # Exit the loop
    else:
        print("Invalid choice, please try again!")
