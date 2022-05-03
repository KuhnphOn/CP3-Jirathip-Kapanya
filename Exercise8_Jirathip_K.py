username = input("USERNAME: ")
password = input("PASSWORD: ")
item_1 = "Doran's Ring"
item_1_price = 400
item_2 = "Doran's Blade"
item_2_price = 450
item_3 = "Doran's Shield"
item_3_price = 450
item_4 = "Tear of the Goddess"
item_4_price = 400
item_5 = "Health Potion"
item_5_price = 50
if (username == "admin" and password == "admin"):
    print("1.)", item_1, item_1_price, "G")
    print("2.)", item_2, item_2_price, "G")
    print("3.)", item_3, item_3_price, "G")
    print("4.)", item_4, item_4_price, "G")
    print("5.)", item_5, item_5_price, "G")
    cart = input("Choose 1 item to buy(enter 1-5): ")
    if cart > "0" and cart <= "5":
        amount = int(input("How much you would like?: "))
        if cart == "1":
            print(item_1, "x", amount)
            print("Total: ", amount * item_1_price)
        elif cart == "2":
            print(item_2, "x", amount)
            print("Total: ", amount * item_2_price)
        elif cart == "3":
            print(item_3, "x", amount)
            print("Total: ", amount * item_3_price)
        elif cart == "4":
            print(item_4, "x", amount)
            print("Total: ", amount * item_4_price)
        elif cart == "5":
            print(item_5, "x", amount)
            print("Total: ", amount * item_5_price, "G")
        else:
            print("ERROR please tryagain")
    else:
        print("CHOOSE BETWEEN 1-5! Tryagain")
else:
    print("Wrong Username or Password")
