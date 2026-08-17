age = int(input("Enter your age: "))
movie_type = input("Choose the movie type (Action/Drama/Horror): ").lower()
show_time = input("Choose the show time (Matinee/Evening/Night): ").lower()

base_price = 300

if movie_type == "action":
    booking_status = "Booking Confirmed"
    movie_price = base_price * 1.5
elif movie_type == "drama":
    booking_status = "Booking Confirmed"
    movie_price = base_price
elif movie_type == "horror" and age > 15:
    booking_status = "Booking Confirmed"
    movie_price = base_price
else:
    booking_status = "Booking Denied: Age restriction for Horror movies."
    movie_price = base_price 

if show_time == "matinee":
    show_time_discount = 0.20
else:
    show_time_discount = 0

final_price = movie_price * (1 - show_time_discount)

print("\nMovie Ticket Booking System")
print("----------------------------")
print(f"Age: {age}")
print(f"Movie Type: {movie_type.capitalize()}")
print(f"Show Time: {show_time.capitalize()}")
print(f"Applicable Discount: {show_time_discount * 100:.0f}%")
print(f"Final Price: Rs. {final_price:.2f}")
print(f"Booking Status: {booking_status}")
