# hiding the implementation details of a class and only showing the essential features to the user.
# abstraction eg -:

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

c1 = Car()
c1.strat()