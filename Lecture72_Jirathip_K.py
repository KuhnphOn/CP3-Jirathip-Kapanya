menuList = []

def showBill():
    total = 0
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        total = total + menuList[i][1]
    print("\nTotal:",total)
        

        
while True:
    menuName = input("Please Enter Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append([menuName,menuPrice])
showBill()
