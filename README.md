# 🧾 Utility Store Billing System

This is a console-based Utility Store Billing System built in Python that allows users to add items with their quantity and price, then automatically calculates the subtotal, sales tax (6.25%), and the total bill. 

## 👨‍💻 Author
**Sadain Ahmad**

## 🚀 Features
- Add multiple items to a bill
- Automatically calculates:
  - Subtotal
  - 6.25% sales tax
  - Total amount
- Neatly formatted bill display

## 🛠️ Technologies Used
- Python 3

## 📦 Program Structure

### `Item` Class
Represents an item with:
- `name`: Name of the item
- `quantity`: Quantity purchased
- `price`: Price per item
- `total`: Total cost for the item (`quantity * price`)

### `Bill` Class
Handles:
- Adding items to the bill
- Calculating subtotal
- Calculating tax (6.25%)
- Calculating total amount
- Displaying the complete bill

## 💡 How to Use

1. Run the script using Python:
```bash
python billing system.py
```
2. Enter the item name, quantity, and price as prompted.

3. When done, type n when asked to add more items.

4. The program will display a full formatted bill including subtotal, tax, and total.

## 📷 Sample Output

Input name of item 1 : Apples

Input quantity of item 1 : 2

Input Price of item 1 : 1.5

Add more item? (y/n) y

Input name of item 2 : Bread

Input quantity of item 2 : 1

Input Price of item 2 : 2.0

Add more item? (y/n) y

Input name of item 3 : Milk

Input quantity of item 3 : 3

Input Price of item 3 : 1.25

Add more item? (y/n) n

Your Bill:

Item--------------------------Quantity--Price-----Total     
Apples------------------------2---------1.5-------3.0       
Bread-------------------------1---------2.0-------2.0       
Milk--------------------------3---------1.25------3.75      

Subtotal------------------------------------------8.75      
6.25% sales tax-----------------------------------0.55       
Total---------------------------------------------9.3        


## 🧹 Notes
- The program runs in a loop, allowing the user to input multiple items.
