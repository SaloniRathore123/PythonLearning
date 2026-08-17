# A nurse takes a patient's temperature repeatedly (simulate with user input) until it drops to
# 98.6°F or below (normal). Print how many temperature readings it took to get back to normal.
reading = 0
while True:
    temperature = float(input("Enter the patient temperature: "))
    reading += 1
    if temperature <= 98.6:
       break
print(f"There are {reading} readings to get back temperature normal.")
