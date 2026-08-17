# A support agent keeps answering calls. After each call, ask "Any more calls waiting?
# (yes/no)". Keep looping while the answer is "yes". Count total calls handled and print it at
# the end.
total_call = 0
while True:
    call = input("Any more call waiting(yes/no): ")
    if call == "no":
       break
    total_call += 1
print(f"Total calls = {total_call}")