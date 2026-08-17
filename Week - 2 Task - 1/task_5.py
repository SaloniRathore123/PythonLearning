# 5. Show a menu that must appear at least once, and let the user exit by choosing option 2
while True:
   print("1. Add\n2. Exit")
   choice = input("Choose: ")
   if choice == "2":
       break