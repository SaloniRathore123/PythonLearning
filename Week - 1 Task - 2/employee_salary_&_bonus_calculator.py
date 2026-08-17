employee_name = input("Enter the employee name: ")
base_salary = int(input("Enter the base salary: "))
year_of_service = int(input("Enter the year of service: "))
rating = int(input("Enter the performance rating(1 - 5): "))

# Bonus rate based on year
if year_of_service < 1:
    bonus_rate = 0
elif year_of_service <= 3:
    bonus_rate = 0.5
elif year_of_service <= 5:
    bonus_rate = 0.10
else:
    bonus_rate = 0.15

# Performance multiplier
if rating <= 2:
    performance_multiplier = 0
elif rating == 3:
    performance_multiplier = 1 
elif rating == 4:
    performance_multiplier = 1.5
else:
   performance_multiplier = 2

# Calculate the bonus
bonus_amount = base_salary * bonus_rate * performance_multiplier

# Calculate the gross salary
gross_salary = base_salary + bonus_amount

# Calculate the deduction
tax = gross_salary * 0.10
insurance = gross_salary * 0.05
total_deductions = tax + insurance

# Calculate the net salary
net_salary = gross_salary - total_deductions

# Performance rating text
if rating == 1:
    rating_txt = "Poor"
elif rating == 2:
    rating_txt = "Below Average"
elif rating == 3:
    rating_txt = "Average"
elif rating == 4:
    rating_txt = "Good"
else:
    rating_txt = "Excellent"

print("\nEmployee Salary Summary")
print("_______________________________________")
print(f"Employee name: {employee_name}")
print(f"Base Salary: {base_salary}")
print(f"Year of Service: {year_of_service}")
print(f"Performace Rating: {rating} ({rating_txt})")
print("________________________________________")
print(f"Bonus Rate: {bonus_rate}")
print(f"Performance Rating: {performance_multiplier}x")
print(f"Bonus Amount: {bonus_amount}")
print("__________________________________________")
print(f"Gross Salary: {gross_salary}")
print(f"Tax (10%): {tax}")
print(f"Insurance (5%): {insurance}")
print(f"Total Deduction: {total_deductions}")
print(f"Net Salary: {net_salary}")










