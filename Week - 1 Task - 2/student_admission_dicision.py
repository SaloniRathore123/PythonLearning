name = input("Enter the student name: ")
math_marks = int(input("Enter the mathematics marks: "))
english_marks = int(input("Enter the english marks: "))
science_marks = int(input("Enter the science marks: "))
interview_score = int(input("Enter the interview score(1 - 10): "))

# Admission Criteria
all_subject = math_marks + english_marks + science_marks
average = all_subject/3

if (math_marks > 75 and english_marks > 75 and science_marks > 75) and interview_score > 7:
    category = "Excellent"  
    admission_status = "Accepted"
elif average > 70 and interview_score >= 6:
    category = "Good"
    admission_status = "Accepted"
elif average > 60 and interview_score >= 5:
    category = "Fair"
    admission_status = "Accepted"
elif average > 50 and interview_score >= 4:
    category = "Waitlist"
    admission_status = "Waitlist"
else:
    category = "Rejected"
    admission_status = "Rejected"

# Merit scholarshit
if category == "Excellent":
    if average > 85 and interview_score == 10:
        scholarship = "100%"
        scholarship_amount = 75000
    elif average > 80 and interview_score > 8:
        scholarship = "75%"
        scholarship_amount = 45000
    elif average > 75:
        scholarship = "50%"
        scholarship_amount = 25000
    else:
        scholarship = "0%"
        scholarship_amount = 0
else:
    scholarship = "Not Applicable"
    scholarship_amount = 0

# Remarks
if category == "Excellent":
    remarks = "Outstanding academic performance with excellent interview!"
elif category == "Good":
    remarks = "Strong academic performance. Welcome to join us!"
elif category == "Fair":
    remarks = "Satisfactory performance. Proceed with admission process."
elif category == "Waitlist":
    remarks = "Your profile is under review. We'll notify you soon."
else:
    remarks = "We encourage you to reapply with improved marks."


print("="*55)
print(f"Student: {name}")
print(f"Math Marks: {math_marks}")
print(f"English Marks: {english_marks}")
print(f"Science Marks: {science_marks}")
print(f"Average Marks: {average:.2f}")
print(f"Interview Score: {interview_score}/10")
print()
print(f"Category: {category} ")
print(f"Admission: {admission_status} ")
print()
if scholarship_amount > 0:
    print(f"Merit Scholarship: {scholarship}")
    print(f"Scholarship Amount: Rs. {scholarship_amount:,.0f}")
else:
    print(f"Merit Scholarship: {scholarship}")

print()
print(f"Remarks: {remarks}")

 