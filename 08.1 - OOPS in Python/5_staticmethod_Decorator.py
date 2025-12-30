class Car:
    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def start():
        return "car started"

    @staticmethod
    def stop():
        return "car stopped"

c1 = Car("Fortuner")
print(c1.name)

print(c1.start())
print(c1.stop())