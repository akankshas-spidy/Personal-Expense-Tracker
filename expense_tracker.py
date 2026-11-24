import csv
import os

FILE = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Please enter a valid amount!")
        return

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    with open(FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(" | ".join(row))

def total_expenses():
    total = 0

    if os.path.exists(FILE):
        with open(FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total += float(row["Amount"])

    print("Total Expenses: ₹", total)

while True:
    print("\n--- PERSONAL EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")