def main():
    print(f" Running Expense Tracker!")

    # Get user input for expense.
    get_user_expense()
    # Write their expense to a file
    save_expense_to_file()
    # Read file summarise expenses.
    summarise_expenses()
    

def get_user_expense():
    print(f"Getting User Expense")
    pass

def save_expense_to_file():
    print(f"Saving User Expense")
    pass

def summarise_expenses():
    print(f"Summarising User Expense")
    pass

if __name__ == "__main__":
    main()