# Week 1 Practice Code: Personal Budget Calculator
name = input("Enter your name: ")
monthly_salary = float(input("Enter your monthly salary: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
number_of_dependents = int(input("Enter the number of dependents: "))
has_savings = input("Do you have savings? (True/False): ").lower() == "true"

remaining_balance = monthly_salary - monthly_expenses
per_dependent_allocation = remaining_balance / number_of_dependents if number_of_dependents > 0 else 0

print(f"\nHello {name}, here is your personal budget summary:")
print(f"Monthly Salary: {monthly_salary:.2f}")
print(f"Monthly Expenses: {monthly_expenses:.2f}")
print(f"Number of Dependents: {number_of_dependents}")
print(f"Remaining Balance: {remaining_balance:.2f}")
print(f"Allocation per Dependent: {per_dependent_allocation:.2f}")
print(f"Savings Status: {'Yes' if has_savings else 'No'}")

