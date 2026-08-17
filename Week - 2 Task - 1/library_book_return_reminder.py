# A user keeps entering book titles they want to return. Stop when they type "done". 
# For every title entered, print "Returned: <title>" . 
# At the end, print the total number of books returned.
total_books = 0
while True:
    title = input("Enter the book title: ")
    if title == "done":
        break
    total_books += 1
    print(f"Returned: {title}")
print(f"Total are {total_books} book.")
