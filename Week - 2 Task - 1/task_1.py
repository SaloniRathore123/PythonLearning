# 1. Print numbers 1 to 30. For multiples of 3 print "Fizz", multiples of 5 print "Buzz",
# multiples of both print "FizzBuzz".

for i in range(1, 30):
   if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
   elif i % 3 == 0:
      print("Fizz")
   elif i % 5 == 0:
      print("Buzz")
   else:
      print(i, end=" , ")
print("Loop end!")
        