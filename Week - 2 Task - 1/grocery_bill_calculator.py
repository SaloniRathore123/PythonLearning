# Scenario: You're at a store. Keep entering item prices. Type 0
# when done. Show the total bill.
# Real-world connection: Cash register / billing systems work exactly like this.
total = 0
while True:
    price = float(input("Enter the price of items and 0 for finish! "))
    if price == 0:
        break
    total += price
print("Your total bill is: ", total)