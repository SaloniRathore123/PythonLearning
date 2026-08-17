# A store has a secret discount code (you decide it in the code, e.g. "SAVE20" ). The user keeps
# guessing. Give them a maximum of 5 attempts. If they guess right before running out, print
# "You won 20% off!" and stop immediately. If they run out of attempts without guessing,
# print "No discount for you."
max_attempt = 5
attempt_used = 0
while attempt_used < max_attempt:
    guess = input("Enter the code you guess: ").upper()
    attempt_used += 1
    if guess == "SAVE20":
        print("You won 20% off")
        break
else:
    print("No dsicount")

    
