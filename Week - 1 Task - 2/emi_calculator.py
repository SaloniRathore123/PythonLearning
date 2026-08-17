aplicant_name = input("Enter the aplicant name: ")
age = int(input("Enter the age: "))
monthly_income = float(input("Enter the monthly income: "))
employee_type = input("Employment Type: (Salaried/Self-Employed/Unemployed): ")
credit_score = int(input("Enter the credit score between (0 - 900): "))
existing_debt = float(input("Enter the existing debt: "))
loan_amount_requested = float(input("Enter the requested loan amount: "))
loan_tenure_in_years = int(input("Enter the load tenure in  years: "))

# Eligiblity Criteria
# Age validation
age_valid = 21 <=  age <= 60

# Employment Validation
employment_valid = employee_type in ['Salaried', "Self-Employed"]

# Credit Score validation
credit_score_valid = credit_score >= 650

# Income verification
income_valid = loan_amount_requested <= (50 * monthly_income)

# Debt Ratio Validation
debt_ratio = existing_debt / monthly_income
debt_valid = existing_debt <= (0.30 * monthly_income) 

is_eligible = age_valid and employment_valid and credit_score_valid and income_valid and debt_valid

# Loan approved category
if is_eligible:
    if (credit_score >= 800 and monthly_income > 100000) and (age <= 40):
        category = "PREMIUM"
        interest_rate = 6
        loan_status = "APPROVED"
    elif credit_score >= 700 and monthly_income > 50000:
        category = "STANDARD"
        interest_rate = 8
        loan_status = "APPROVED"
    else:
        category = "BASIC"
        interest_rate = 11
        loan_status = "APPROVED"
else:
    category = "N/A"
    interest_rate = 0
    loan_status = "REJECTED"

# EMI Calculation
# Formula = EMI = (P × R × (1 + R)^N) / ((1 + R)^N - 1)
# Where:
# P = Principal (loan amount)
# R = Monthly interest rate (annual rate / 12 / 100)
# N = Total number of months (tenure in years × 12)

if loan_status == "APPROVED":
    monthly_interest_rate = interest_rate / 12 / 100
    total_months = loan_tenure_in_years * 12
    emi = (loan_amount_requested * monthly_interest_rate * (1 + monthly_interest_rate)** total_months) / ((1 + monthly_interest_rate)**total_months - 1)
    total_amount = emi * total_months
    total_interest = total_amount - loan_amount_requested
else:
    emi = 0
    total_amount = 0
    total_interest = 0


rejection_reasons = []
if not age_valid:
    rejection_reasons.append("Age must be between 21 to 60 years")
if not employment_valid:
    rejection_reasons.append("Employement must be Salaried or Self-Employed")
if not credit_score_valid:
    rejection_reasons.append(f"Credit score must be minimum 650 (Current: {credit_score})")
if not income_valid:
    rejection_reasons.append(f"Loan amount exceeds 50x monthly income limit (Current Validation: {monthly_income})")
if not debt_valid:
    rejection_reasons.append(f"Existing debt exceeds 30% of monthly income (Current Debt Validation: {debt_valid})")

# Rmarks
if loan_status == "APPROVED":
    if category == "PREMIUM":
        remarks = "Congratulation! You are approved for premium loan."
    elif category == "STANDARD":
        remarks = "Congratulation! You are approved for standard loan."
    else:
        remarks = "Congratulation! You are approved for basic loan."
else:
    remarks = "Please reapply when you meet all eligiblity criteria."

# Summary
print("Bank Loan Application")
print(f"Application Name: {aplicant_name}")
print(f"Age: {age}")
print(f"Monthly Income: {monthly_income}")
print(f"Employement Type: {employee_type}")
print(f"Credit Score: {credit_score}")
print(f"Existing Debt: {existing_debt}")
print("")
print("Eligiblity Check")
print(f"Age (21 - 60): {'Valid' if age_valid else 'Invalid'}")
print(f"Employement: {'Valid' if employment_valid else 'Invalid'}")
print(f"Credit Score: {'Valid' if credit_score_valid else 'Invalid'}")
print(f"Income Verification: {'Valid' if income_valid else 'Invalid'}")
print(f"Debt Ratio: {'Valid' if debt_valid else 'Invalid'}")
print("")
print("Loan Decision")
if loan_status == "APPROVED":
    print(f"Loan Status: APPROVED")
    print(f"Category: {category}")
    print(f"Interest Rate: {interest_rate}% per annum")
    print(f"Requested Amount: Rs. {loan_amount_requested:,.2f}")
    print(f"Tenure: {loan_tenure_in_years} years")
    print()
# ===== EMI DETAILS =====
    print("=== EMI DETAILS ===")
    print(f"Monthly EMI: Rs. {emi:,.2f}")
    print(f"Total Amount to Pay: Rs. {total_amount:,.2f}")
    print(f"Total Interest Paid: Rs. {total_interest:,.2f}")
    print()
else:
    print(f"Loan Status: REJECTED ")
    print()

    print("Reasons for Rejection:")
    for i, reason in enumerate(rejection_reasons, 1):
        print(f"  {i}. {reason}")
        print()
print(f"Remarks: {remarks}")






