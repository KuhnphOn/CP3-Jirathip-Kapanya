menuList = []
priceList = []

def showBill():
    total = 0
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        total = total + priceList[i]
    print("\nTotal:",total)
        

        
while True:
    menuName = input("Please Enter Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
