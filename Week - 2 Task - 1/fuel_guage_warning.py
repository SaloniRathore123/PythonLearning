# A car's fuel starts at 100%. Each "trip" (loop round), 
# ask how much fuel was used (userenters a number), and subtract it. 
# Keep looping until fuel drops to 20% or below, then print "Refuel now!"
#  along with how many trips were taken
fuel = 100
trips = 0
while True:
    fuel_used = float(input("How much fuel used? "))
    fuel -= fuel_used
    trips += 1
    if fuel <= 20:
        print(f"Now fuel is {fuel}")
        break
print(f"Total trips are {trips}")
        