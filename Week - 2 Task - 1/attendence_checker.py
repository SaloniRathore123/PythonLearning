present = 0
absent = 0
total_student = 10

for students in range(1, total_student + 1):
    status = input(f"{students} - Present or Absent (P/A) = ").upper()
    if status == "P":
        present += 1
    elif status == "A":
        absent += 1
    else:
        print("Invalid entert!")
        continue
percentage = (present/total_student)*100
print(f"Total Present = {present}")
print(f"Total Absent = {absent}")
print(f"Total Present Percentage = {percentage}")