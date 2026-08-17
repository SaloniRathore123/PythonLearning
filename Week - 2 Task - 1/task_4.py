# 4. Print only the vowels in a given word.
word = "education"
for ch in word:
    if ch not in "aeiou":
        continue
    print(ch)