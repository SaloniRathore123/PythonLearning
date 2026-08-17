# 3. Find the first number in a list divisible by 7, then stop searching.
numbers = [6, 13, 14, 50]
for i in numbers:
    if i % 7 == 0:
        print(i)
        break