def login():
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")
    if usernameInput == "username" and passwordInput == "password":
        return True
    else:
        return False


def show_menu():
    print("--- SecretShop ---")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menu_select()


def menu_select():
    userSelected = int(input(">> "))
    if userSelected == 1:
        price = int(input("Enter price(THB): "))
        print("Total:", vat_cal(price))
    elif userSelected == 2:
        print("Total (include vat):", price_cal())
    else:
        print("ERROR please try again.")
        show_menu()


def vat_cal(price):
    vat = 7
    result = price + (price * vat / 100)
    return round(result)


def price_cal():
    price1 = int(input("Enter first price: "))
    price2 = int(input("Enter second price: "))
    return vat_cal(price1 + price2)


i = True
while i:
    if login():
        show_menu()
        i = False
    else:
        print("----------------------------")
        print("Invalid username or password")
        print("----------------------------")
