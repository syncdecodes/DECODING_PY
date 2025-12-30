class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s = Student("Aman", 12)
print(s.name, s.roll)



class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"Student: {self.name}, Roll: {self.roll}"

s = Student("Aman", 12)
print(s)



class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __repr__(self):
        return f"Student({self.name!r}, {self.roll})"

s = Student("Aman", 12)
print(repr(s))



class Student:
    def __init__(self, stud):
        self.students = stud
    def __len__(self):
        return len(self.students)
s1 = Student([1, 2, 3])
print(len(s1))



class Box:
    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        return self.size == other.size

b1 = Box(10)
b2 = Box(10)
print(b1 == b2)



class Marks:
    def __init__(self, m):
        self.m = m

    def __add__(self, othe):
        return self.m + othe.m

m1 = Marks(50)
m2 = Marks(30)
print(m1 + m2)



class Data:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

d = Data([10, 20, 30])
print(d[1])



class Data:
    def __init__(self, items):
        self.items = items
    
    def __setitem__(self, index, value):
        self.items[index] = value

d = Data([10, 20, 30])
d[1] = 200
print(d.items)



class Test:
    def __del__(self):
        print("Object destroyed")

t = Test()
del t



class Hello:
    def __call__(self):
        print("Object is called like a function")

h = Hello()
h()



class MyList:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

ml = MyList([1, 2, 3])
for x in ml:
    print(x)