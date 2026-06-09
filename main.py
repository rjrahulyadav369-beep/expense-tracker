import os
FILE = "expenses.txt"

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(FILE, "a") as f:
        f.write(f"{name},{amount}\n")

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")
    total = 0

    with open(FILE, "r") as f:
        for line in f:
            name, amount = line.strip().split(",")
            print(f"{name} : ₹{amount}")
            total += float(amount)

    print("---------------------")
    print("Total Expense: ₹", total)

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()