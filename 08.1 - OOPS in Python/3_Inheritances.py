# single inheritance (single child class inherits from single parent class)

class Car:

    @staticmethod
    def start():
        return "car started"

    @staticmethod
    def stop():
        return "car stopped"

class ToyotaCar(Car): # now class ToyotaCar has access to all the methods present in Car
    def __init__(self, name):
        self.name = name

c1 = ToyotaCar("Fortuner")
print(c1.name)

print(c1.start())
print(c1.stop())



# multi level inheritance (a class is derived from another derived class, forming a chain of inheritance)

class Car:

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car): # now class ToyotaCar has access to all the methods present in Car
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

c1 = Fortuner("electric vehicle")
c1.start()



# multiple inheritance (a new child class inherits attributes and methods from more than one parent class)

class A:
    varA = "welcome A" # class variables
class B:
    varB = "welcome B" # class variables
class C(A, B):
    varC = "welcome C" # class variables


var = C()
print(var.varA)
print(var.varB)
print(var.varC)