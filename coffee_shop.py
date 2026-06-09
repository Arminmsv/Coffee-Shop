menu = {"Cakes" : {"Chocolate cake" : 120000 ,
                   "Nutella cake" : 140000 ,
                   "Tiramisu cake" : 145000 ,
                   "Strawberry cake" : 120000} ,
        "Cold drinks" : {"Beer" : 70000 ,
                        "ice tea" : 60000 ,} ,
        "Hot drinks" : {"Tea" : 50000 ,
                       "Hot chocolate" : 110000 ,
                        "Coffee" : 70000 }}


print("Welcome to Coffee Shop")
for category , detail in menu.items():
    print(" ")
    print("\n" + category , ":")
    for item , price in detail.items():
        print(item , price)

total_price = 0
more = "yes"

while more in ["yes" , "y"]:
    order = input(" What do you want? ").strip().lower()

    found = False

    for category , detail in menu.items():
        for item , price in detail.items():
            if order == item.lower():
                found = True
                counter_order = int(input(" How many? "))
                total_price += counter_order * price
    if not found:
        print(" Sorry we dont have this item!")
    more = input(" Anything else? (yes/no): ").strip().lower()

print(f" you have to pay: {total_price:,}")
print(" Your order has been registered successfully ✅")
print(" Thank you for visiting our coffee shop! ☕") 
