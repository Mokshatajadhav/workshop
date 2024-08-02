import csv
import os
from datetime import datetime

# File path for the inventory file
INVENTORY_FILE = 'inventory.csv'

# Initialize inventory file with headers if it doesn't exist
def initialize_inventory_file():
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ItemID', 'ItemName', 'Category', 'Quantity', 'Price', 'ExpirationDate'])

# Function to add a new item to the inventory
def add_item(item_id, item_name, category, quantity, price, expiration_date):
    try:
        with open(INVENTORY_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([item_id, item_name, category, quantity, price, expiration_date])
        print(f"Item {item_name} added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

# Function to update an existing item's quantity, price, or expiration date
def update_item(item_id, quantity=None, price=None, expiration_date=None):
    try:
        updated = False
        rows = []
        with open(INVENTORY_FILE, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                if row[0] == item_id:
                    if quantity is not None:
                        row[3] = quantity
                    if price is not None:
                        row[4] = price
                    if expiration_date is not None:
                        row[5] = expiration_date
                    updated = True
                rows.append(row)
        
        if updated:
            with open(INVENTORY_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)
            print(f"Item {item_id} updated successfully.")
        else:
            print(f"Item {item_id} not found.")
    except Exception as e:
        print(f"Error updating item: {e}")

# Function to view the entire inventory
def view_inventory():
    try:
        with open(INVENTORY_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except Exception as e:
        print(f"Error viewing inventory: {e}")

# Function to delete an item from the inventory
def delete_item(item_id):
    try:
        deleted = False
        rows = []
        with open(INVENTORY_FILE, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                if row[0] == item_id:
                    deleted = True
                    continue
                rows.append(row)
        
        if deleted:
            with open(INVENTORY_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)
            print(f"Item {item_id} deleted successfully.")
        else:
            print(f"Item {item_id} not found.")
    except Exception as e:
        print(f"Error deleting item: {e}")

# Function to check for and remove expired items
def check_expired_items():
    try:
        today = datetime.today().strftime('%Y-%m-%d')
        rows = []
        expired_items = []
        with open(INVENTORY_FILE, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                try:
                    expiration_date = datetime.strptime(row[5], '%Y-%m-%d').strftime('%Y-%m-%d')
                    if expiration_date < today:
                        expired_items.append(row)
                    else:
                        rows.append(row)
                except ValueError:
                    print(f"Invalid date format for item {row[1]}: {row[5]}")
        
        if expired_items:
            with open(INVENTORY_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)
            print("Expired items removed:")
            for item in expired_items:
                print(', '.join(item))
        else:
            print("No expired items found.")
    except Exception as e:
        print(f"Error checking expired items: {e}")

# Main program loop for user interaction
def main():
    initialize_inventory_file()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Delete Item")
        print("5. Check Expired Items")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_id = input("Enter Item ID: ")
            item_name = input("Enter Item Name: ")
            category = input("Enter Category: ")
            quantity = input("Enter Quantity: ")
            price = input("Enter Price: ")
            expiration_date = input("Enter Expiration Date (YYYY-MM-DD): ")
            add_item(item_id, item_name, category, quantity, price, expiration_date)
        
        elif choice == '2':
            item_id = input("Enter Item ID to update: ")
            quantity = input("Enter new Quantity (leave blank if no change): ")
            price = input("Enter new Price (leave blank if no change): ")
            expiration_date = input("Enter new Expiration Date (leave blank if no change): ")
            update_item(item_id, quantity if quantity else None, price if price else None, expiration_date if expiration_date else None)
        
        elif choice == '3':
            view_inventory()
        
        elif choice == '4':
            item_id = input("Enter Item ID to delete: ")
            delete_item(item_id)
        
        elif choice == '5':
            check_expired_items()
        
        elif choice == '6':
            print("Exiting Inventory Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
