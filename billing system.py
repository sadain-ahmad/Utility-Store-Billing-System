class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = round((quantity * price), 2)

class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.total for item in self.items)
    
    def calculate_tax(self):
        return round((self.calculate_subtotal() * 0.0625), 2)
    
    def calculate_Total(self):
        return round((self.calculate_subtotal() + self.calculate_tax()), 2)
    
    def display(self):
        print("\nYour Bill:\n")
        print(f"{'Item':<30}{'Quantity':<10}{'Price':<10}{'Total':<10}")

        for item in self.items:
            print(f"{item.name:<30}{item.quantity:<10}{item.price:<10}{item.total:<10}")

        print(f"\n{'Subtotal':<50}{self.calculate_subtotal():<10}")
        print(f"{'6.25% sales tax':<50}{self.calculate_tax():<10}")
        print(f"{'Total':<50}{self.calculate_Total():<10}")


bill = Bill()

print("""
        ********************************************************
        ********************************************************
        *****                                              *****
        *****           MADE BY : SADAIN AHMAD             *****
        *****                                              *****
        ********************************************************
        ********************************************************

""")

while True:
    name = input(f"Input name of item {i} : ")
    quantity = int(input(f"Input quantity of item {i} : "))
    price = float(input(f"Input Price of item {i} : "))
    item = Item(name, quantity, price)
    bill.add_item(item)
    sentinal = input("Add more item? (y/n)")
    if sentinal=="n":
        break


bill.display()