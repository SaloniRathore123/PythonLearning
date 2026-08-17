account_balance = 1000
invalid_attempts = 0

while True:
    amount = float(input("Enter the withdrwal amount (-1 for exit): "))
    if amount == -1:
        print(f"You exit from system! You final amount is: ${account_balance}")
        break

    if amount % 10 != 0:
        print(f"Amount must be multiple of $10.")
        invalid_attempts += 1
    elif amount > account_balance:
        print(f"Insufficient funds!")
        invalid_attempts += 1
    else:
        account_balance -= amount
        print(f"Withdrwal successful and the new balance is: ${account_balance}")
        invalid_attempts = 0
        continue

    if invalid_attempts >= 3:
        print("To many invalid attempts. Account blocked!")
        break