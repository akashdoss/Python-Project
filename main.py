import csv
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Bills): ")
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, desc])

    print("Expense added!\n")


def view_summary():
    data = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames:
            reader.fieldnames = [h.strip() for h in reader.fieldnames]

        for row in reader:
            category = row.get("Category")
            amount = row.get("Amount")

            if not category or not amount:
                continue

            amount = float(amount)

            if category in data:
                data[category] += amount
            else:
                data[category] = amount

    print("\n--- Category Summary ---")
    for cat, amt in data.items():
        print(f"{cat}: ₹{amt}")

    if data:
        max_cat = max(data, key=data.get)
        print(f"\nHighest spending: {max_cat} (₹{data[max_cat]})")


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames:
            reader.fieldnames = [h.strip() for h in reader.fieldnames]

        for row in reader:
            date = row.get("Date")
            amount = row.get("Amount")

            if not date or not amount:
                continue

            if date.startswith(month):
                total += float(amount)

    print(f"\nTotal expenses for {month}: ₹{total}")


def plot_chart():
    data = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames:
            reader.fieldnames = [h.strip() for h in reader.fieldnames]

        for row in reader:
            category = row.get("Category")
            amount = row.get("Amount")

            if not category or not amount:
                continue

            data[category] = data.get(category, 0) + float(amount)

    if not data:
        print("No data to show.")
        return

    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()


def menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Category Summary")
        print("3. Monthly Summary")
        print("4. Show Pie Chart")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            plot_chart()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    init_file()
    menu()