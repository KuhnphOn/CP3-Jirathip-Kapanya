class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnACon(self):
        print("AC : On")
        
class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class Truck(Vehicle):
    pass
        
class Van(Vehicle):
    pass
        
class EstateCar(Vehicle):
    pass
        

car1 = Car()
car1.turnACon()
car1.sayHello()

truck1 = Truck()
truck1.turnACon()

van1 = Van()
van1.turnACon()

estateCar1 = EstateCar()
estateCar1.turnACon()