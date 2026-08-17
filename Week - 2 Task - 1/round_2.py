# 8. Keep asking the user "Continue? (yes/no)" until they type "no".
print("Question - 8")
while True:
    user = input("Enter the yes (no for exit): ")
    if user == "no":
        break
print("Loop Terminate")

# 9. Ask the user to guess a number. Keep asking until they guess correctly 
# (you decide the secret number in the code, e.g. 7).
print("Question - 9")
while True:
    guess_number = int(input("Guess the number: "))
    if guess_number == 7:
        print("You win!")
        break
    else:
        print("You guess the wrong number. Please try again!!!")
        
# 10. Add numbers the user enters, one at a time, until they enter a negative number.
print("Question - 10")
sum = 0
while True:
    num = int(input("Enter the numbers: "))
    if num < 0:
        break
    sum += num
print(f"Total sum is: {sum}")

# 11. Keep doubling a number starting from 1 (1, 2, 4, 8...) until it's bigger than 1000. Print how many steps it took.
print("Question - 11")
step = 0
num = 1
while num <= 1000:
    num = num * 2
    step += 1
print(f"Last number: {num}")
print(f"Total steps: {step}")

# 12. Ask the user to enter a word repeatedly until they type a word with more than 5 letters.
print("Question - 12")
while True:
    word = input("Enter the word (more tha 5 letter for stop): ")
    if len(word) > 5:
        break
print(f"The loop stop word is: {word}")
