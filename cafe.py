import json
import atexit

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Cafe:
    def __init__(self):
        self.menu = {}
        self.orders = []
        self.tables = {}
        self.order_history = []

        self.load_data_from_json()  # Load data from JSON file on program start
        atexit.register(self.save_data_to_json)  # Auto-save data when the program exits

    def add_menu_item(self, name, price):
        self.menu[name] = MenuItem(name, price)

    def take_order(self, table_number, items):
        order = Order(table_number)
        for item_name in items:
            if item_name in self.menu:
                order.add_item(item_name)
            else:
                print(f"{item_name} is not on the menu.")
        self.orders.append(order)
        self.tables[table_number] = "Occupied"

    def close_order(self, table_number):
        for order in self.orders:
            if order.table_number == table_number:
                self.orders.remove(order)
                self.tables[table_number] = "Vacant"
                total_cost = sum(self.menu[item_name].price for item_name in order.items)
                receipt = {
                    "Table Number": table_number,
                    "Items": order.items,
                    "Total Cost": total_cost
                }
                self.order_history.append(receipt)
                print(f"Table {table_number}'s order has been closed. Total cost: ${total_cost:.2f}")

    def load_data_from_json(self):
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
                self.menu = {name: MenuItem(name, price) for name, price in data.get("Menu", {}).items()}
                self.order_history = data.get("Order History", [])
                self.tables = data.get("Table Status", {})
        except FileNotFoundError:
            print("No data file found. Starting with empty data.")

    def save_data_to_json(self):
        data = {
            "Menu": {item.name: item.price for item in self.menu.values()},
            "Order History": self.order_history,
            "Table Status": self.tables
        }
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

def print_receipt(order, cafe):
    print(f"Receipt for Table {order['Table Number']}:")
    total_cost = 0
    for item_name in order['Items']:
        item_price = cafe.menu[item_name].price
        total_cost += item_price
        print(f"{item_name}: ${item_price:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

def main():
    cafe = Cafe()

    while True:
        print("1. Add Menu Item")
        print("2. Take Order")
        print("3. Close Order")
        print("4. View Menu")
        print("5. View Table Status")
        print("6. Print Receipt")
        print("7. Exit")
        choice = input("Select an option (1/2/3/4/5/6/7): ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            cafe.add_menu_item(name, price)
        elif choice == "2":
            table_number = int(input("Enter the table number: "))
            items = input("Enter the items (comma-separated): ").split(',')
            cafe.take_order(table_number, items)
        elif choice == "3":
            table_number = int(input("Enter the table number to close the order: "))
            cafe.close_order(table_number)
        elif choice == "4":
            print("Menu:")
            for item_name, item in cafe.menu.items():
                print(f"{item_name}: ${item.price:.2f}")
        elif choice == "5":
            print("Table Status:")
            for table, status in cafe.tables.items():
                print(f"Table {table}: {status}")
        elif choice == "6":
            for order in cafe.order_history:
                print_receipt(order, cafe)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
