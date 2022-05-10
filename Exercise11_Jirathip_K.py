lvl = int(input("How much level of pyramid do you want: "))
for i in range(lvl):
    print(" "*(lvl-i), "*"*(2*i-1))
