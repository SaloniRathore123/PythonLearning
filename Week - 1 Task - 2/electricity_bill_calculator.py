customer_name = input("Enter your name: ")
units_consumed = float(input("Enter the number of units consumed: "))
customer_type = input("Enter customer type (residential/commercial): ").lower()
age = int(input("Enter your age: "))

if customer_type == "residential":
    if units_consumed <= 100:
        rate = 5
    elif units_consumed <= 200:
        rate = 7
    else:
        rate = 100
else:
    if units_consumed <= 100:
        rate = 8
    elif units_consumed <= 300:
        rate = 10
    else:
        rate = 12

base_amount = units_consumed * rate

if units_consumed > 300:
    surcharge = base_amount * 0.20
else:
    surcharge = 0

subtotal = base_amount + surcharge

if age > 60:
    discount = subtotal * 0.15
    print(f"Senior citizen get a discount of {discount:.2f}")
else:
    discount = 0

final_bill = subtotal - discount

print("\nElectricity Bill Summary")
print("-------------------------")
print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {units_consumed}")
print(f"Customer Type: {customer_type.capitalize()}")
print(f"Customer Age: {age}")
print(f"Base Amount: Rs. {base_amount:.2f}")
print(f"Surcharge: Rs. {surcharge:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Final Bill: Rs. {final_bill:.2f}")