class Customer:
    name = ""
    lastName = ""
    age = 0
    
    def addCart(self):
        print("Added",self.name,self.lastName+"'s items to Cart")

customer1 = Customer()
customer1.name = "T4E"
customer1.lastName = "R7U"
customer1.addCart()

customer2 = Customer()
customer2.name = "Z4I"
customer2.lastName = "R7U"
customer2.addCart()

customer3 = Customer()
customer3.name = "Kuhn"
customer3.lastName = "R7U"
customer3.addCart()

customer4 = Customer()
customer4.name = "P4N"
customer4.lastName = "R7U"
customer4.addCart()