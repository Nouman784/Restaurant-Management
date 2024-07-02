'''
Resturant Managment.
'''
menu={
    "pizza":1000,
    "burger":200,
    "shwarma":150,
    "Salad":100,
    "Coke":70,}

print("welcom to Apna Resturant.")
print("We are here for taking your order: Here's the menue: ")

print("pizza:RS-1000\nburger:RS-200\nshwarma:RS-150\nSalad:RS-100\nCoke:RS-70")
order_total=0
Order_1=input("enter the name of item that you want to order :")
if Order_1 in menu:
    order_total+=menu[Order_1]
    print(f"your item {Order_1} has been added to order")
else:
    print(f"your item {Order_1} is not available yet")
    
another_item=input("Do you want to add another item?(yes/No)")
if another_item =="yes":
    Order_2=input("enter the name of the second item :")
    if Order_2 in menu:
        order_total+=menu[Order_2]
        print(f"item {Order_2} has been added to order")
    else:
        print(f"order item {Order_2} is not avoilable!")
print(f"The total amount of items to pay is {order_total}")

