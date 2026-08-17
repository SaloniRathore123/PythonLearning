total = 0
count = 0
for items in range(1, 6):
    items = float(input(f"Enter the item {items} price: $"))
    total += items

    if items >= 20:
       count += 1
    
print(f"The {count} items are expensive")     
print(f"Total price of 5 items are: ${total}")