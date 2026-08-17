# 2. Ask the user for numbers repeatedly and sum them, stopping when they enter 0.
num = int(input("Enter the number (0 to stop): "))
total = 0
while num != 0:
    total += 1
    num = int(input("Enter a number (0 to stop): "))
print("Total:", total)