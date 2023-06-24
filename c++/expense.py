# Assignment2_DDDDDDDDD.py (replace DDDDDDDDD with your student number)
# Full Name: [Your Full Name]
# Student Number: [Your Student Number]

# Function to validate expense name
def validate_expense_name(expense_name):
    if len(expense_name) < 3:
        return False
    return True

# Function to validate expense quantity
def validate_expense_quantity(expense_quantity):
    if expense_quantity < 1:
        return False
    return True

# Function to validate expense total price
def validate_expense_price(expense_price):
    if expense_price < 0.01:
        return False
    return True

# Function to validate expense category
def validate_expense_category(expense_category):
    accepted_categories = ['Food', 'Transportation', 'Entertainment', 'Bills', 'Education']
    if expense_category not in accepted_categories:
        return False
    return True

# Get user's income per chosen time unit
income_per_unit = float(input("How much income do you make per (second, minute, hour, daily, weekly, bi-weekly, trimester, or semi-annual)? "))

# Calculate annual income
annual_income = income_per_unit * 365 * 24 * 60 * 60

# Store and output annual income
annual_income = round(annual_income, 2)
print("Your annual income is:", annual_income)

# Calculate monthly income
monthly_income = annual_income / 12

# Initialize dictionary to store expenses
expenses = {}

# Continuously ask for expenses until monthly budget is surpassed
monthly_budget = monthly_income
while monthly_budget >= 0:
    # Ask for expense details
    expense_name = input("Enter the name of the expense: ")
    expense_quantity = int(input("Enter the quantity of the expense: "))
    expense_price = float(input("Enter the total price of the expense: "))
    expense_category = input("Enter the category of the expense: ")

    # Validate expense details using respective functions
    if (
        validate_expense_name(expense_name)
        and validate_expense_quantity(expense_quantity)
        and validate_expense_price(expense_price)
        and validate_expense_category(expense_category)
    ):
        # Check for duplicate entries
        expense_key = (expense_name, expense_category)
        if expense_key in expenses:
            print("Duplicate entry ignored.")
        else:
            # Store the expense in the dictionary
            expenses[expense_key] = {
                'name': expense_name,
                'quantity': expense_quantity,
                'price': expense_price,
                'category': expense_category
            }

            # Update monthly budget
            monthly_budget -= expense_price
    else:
        print("Invalid expense details. Expense ignored.")

# Output all expenses from each category
for category in set(expense[0][1] for expense in expenses.keys()):
    print(f"Expenses in {category}:")
    for expense in expenses.values():
        if expense['category'] == category:
            print(f"Name: {expense['name']}, Quantity: {expense['quantity']}, Total Price: {expense['price']:.2f}")

# Output all unique expense names
unique_expense_names = set(expense['name'] for expense in expenses.values())
print("Unique expense names:", unique_expense_names)

# Output expense names with the same quantity for all categories
shared_quantity_expenses = []
for expense_name in unique_expense_names:
    quantity = expenses[next(iter(expenses))]['quantity']  # Get quantity of the first expense
   
