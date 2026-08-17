customer_name = input("Enter the customer name: ")
cart_amount = int(input("Enter the total amount: "))
premium_member = input("Is premium member(yes/no): ").lower() == "yes"
has_coupons = input("Has coupons(yes/no): ").lower() == "yes"

# Discount rule
if cart_amount > 20000:
    discount = 0.15
elif cart_amount > 10000:
    discount = 0.10
elif cart_amount > 5000:
    discount = 0.05
else:
    discount = 0

discount_amount = cart_amount * discount
after_discount_amount = cart_amount - discount_amount


# Premium member discount
if premium_member:
    premium_discount = cart_amount * 0.05
else:
    premium_discount = 0

after_premium_discount = cart_amount - discount_amount - premium_discount

# Coupons validation and discount
if has_coupons and cart_amount > 1000 and (premium_member or cart_amount > 5000):
   coupon_discount = 500
   coupon_valid = True
else:
   coupon_discount = 0
   coupon_valid = False

# Subtotal
total_discount = discount_amount + premium_discount + coupon_discount
subtotal = cart_amount - total_discount

# Shipping
if cart_amount > 10000:
    shipping = 0
    shipping_status = "FREE"
else:
    shipping = 250
    shipping_status = "Rs. 250"

# GST
gst = (subtotal + shipping) * 0.05

# Final amount
final_amount = subtotal + shipping + gst

print()
print("======================")
print("Order Summary")
print("======================")
print(f"Customer name: {customer_name}")
print(f"Original Cart Total: {cart_amount}")
print(f"\nDiscount Breakdown")
if discount_amount > 0:
    discount_percentage = discount * 100
    print(f" - Amount Based ({discount_percentage:.0f}%): Rs. {discount_amount:.2f}")
if premium_discount > 0:
    print(f" - Premium Member (5%): Rs. {premium_discount:.2f}")
if coupon_valid:
    print(f" - Coupons Discount: Rs. {coupon_discount:.2f}")
else:
    if has_coupons:
        print(f" - Coupon: Not Applicable")

print(f"Total Discount: Rs. {total_discount:.2f}")
print()
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Shipping Status: {shipping_status}")
print(f"GST(5%): Rs. {gst:.2f}")
print()
print(f"Final Amount: Rs. {final_amount:.2f}")

