class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def FullName(self):
        return f"{self.brand} {self.model}"

# INHERITANCE
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model) # we have already initialized everything in top level so...
        self.batterySize = batterySize


myNewCar = ElectricCar("Mahindra", "BE 9", "79kWH")
print(myNewCar.batterySize)
print(myNewCar.FullName())



# myCar = Car("Tesla", "Roadster")
# # print(myCar)
# print(myCar.brand)
# print(myCar.model)
# print(myCar.FullName())


# #  __init__ => constructor - runs at the very first


# if i use __brand then it becomes private which means we can only access brand in classes and not in the objects / vars as car.brand
#  this privatisation is termed as ENAPSULAITON - private to world but known to the classes (own people)
# we need to make a seperate function for those such as get_brand famously termed as getter

# DECORATORS
# if we need some logic where the class Car itself can acces a method but the Objects cannot we use sth called @staticmethod -> a Decorator
# these all are done so users cannot directly change our variables.

#
