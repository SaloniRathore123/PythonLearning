student_name = input("Enter the student name: ")
marks_obtained = float(input("Enter the marks obtained: "))
attendance_percentage = float(input("Enter the attendance percentage: "))
financial_aid = input("Do you have financial aid? (yes/no): ").lower() == "yes"

if marks_obtained >= 90:
    grade = "A"
elif marks_obtained >= 80:
    grade = "B"
elif marks_obtained >= 70:
    grade = "C"
elif marks_obtained >= 60:
    grade = "D"
else:
    grade = "F"

is_eligible = (marks_obtained >= 80) and (attendance_percentage >= 85) and (not financial_aid)

if is_eligible:
    feedback = "Excellent performance! You qualify for the scholarship."
elif marks_obtained < 80:
    feedback = "You need to improve your marks to qualify for the scholarship."
elif attendance_percentage < 85:
    feedback = "You need to improve your attendance to qualify for the scholarship."
else:
    feedback = "You are not eligible for the scholarship due to financial aid."

print("\nStudent Grade and Scholarship Checker")
print(f"Student Name: {student_name}")
print(f"Marks Obtained: {marks_obtained}")
print(f"Attendance Percentage: {attendance_percentage}")
print(f"Grade: {grade}")
print(f"Financial Aid: {'Yes' if financial_aid else 'No'}")
print(f"Feedback: {feedback}")