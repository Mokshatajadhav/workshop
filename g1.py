# Function to read inventory from a file
def read_inventory(file_path):
    inventory = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, quantity, price = line.strip().split(',')
                inventory[name] = {'quantity': int(quantity), 'price': float(price)}
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return inventory

# Function to display the inventory
def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for name, data in inventory.items():
        print(f"{name}: {data['quantity']} @ ${data['price']:.2f}")

# Function to add or update an item in the inventory
def add_or_update_item(inventory):
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory[name] = {'quantity': quantity, 'price': price}

# Function to remove an item from the inventory
def remove_item(inventory):
    name = input("Enter item name to remove: ")
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print(f"Error: {name} not found in inventory.")

# Function to save inventory to a file
def save_inventory(inventory, file_path):
    with open(file_path, 'w') as file:
        for name, data in inventory.items():
            file.write(f"{name},{data['quantity']},{data['price']}\n")
    print("Inventory saved.")

# Main function to manage the inventory
def main():
    file_path = 'inventory.txt'
    inventory = read_inventory(file_path)
    
    while True:
        print("\n1. Display Inventory\n2. Add/Update Item\n3. Remove Item\n4. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_or_update_item(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            save_inventory(inventory, file_path)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

