# 1. Print the numbers 1 to 10.
for i in range(1,11):
    print(i, end=",")

# 2. Print the numbers 10 down to 1 (countdown).
print("")
for i in range(10, 0, -1):
    print(i, end=",")

# 3. Print all even numbers from 2 to 20.
print("")
for i in range(2, 21):
    if i % 2 == 0:
        print(i, end="-")

# 4. Add up the numbers 1 to 100 and print the total.
print("")
total = 0
for i in range(1, 101):
    total +=i
print("Sum of (1 to 100) numbers = ", total)

# 5. Print each letter of the word "python" on its own line.
ch = "python"
for char in ch:
    print(char)

# 6. Print each letter of "python" backwards.
print("")
string = "python"
for char in reversed(string):
    print(char, end="")

# 7. Count how many letters are in a word entered by the user (without using len()).
print("")
letter = input("Enter the letters: ")
count = 0
for letters in letter:
    count += 1
print(f"Total letter are - {count}")