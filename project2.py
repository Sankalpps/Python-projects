menu={
    'Pizza':40,'pizza':40,
    'Pasta':50,'pasta':50,
    'Burger':60,'burger':60,
    'Salad':70,'salad':70,
    'Coffee':80,'coffee':80
}
print("Welcome to our restaurant.Here's the menu:")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCofee: Rs80")
order_total=0
first_order=input("Enter the first item you want to order =")
if first_order in menu:
    order_total=+menu[first_order]
    print("Order of",first_order,"has been added")
else:
    print(f"The item({first_order})you requested is not avilable")

second_order=input("Do you want to order anything else? (Yes/No)")
if second_order=="Yes" or second_order=="yes":
    second_order=input("Enter the second item")
    if second_order in menu:
        order_total += menu[second_order]
        print("Order of second_order has been added")
    else:
        print(f"The item({second_order})you requested is not avilable")

print(f"The total cost is{order_total}")
