def vat_cal(price):
    vat = price*1.07
    return round(vat)


total = int(input("Enter price: "))
print("Total (include vat):", vat_cal(total))
