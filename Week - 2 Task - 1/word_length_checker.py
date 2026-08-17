word = input("Enter the word with (6 or few characters): ")
count = 0
for ch in word:
    count += 1

if count <= 6:
    print(f"Valid username - {word}")
else:
    print("Too Long!")