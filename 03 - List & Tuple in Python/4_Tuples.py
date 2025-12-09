print("List are mutable but Tuples are immutable just like strings")
tup = (12, 14, 96, 75, 20, 65)
print(tup)
print(tup[1])

"""
tup[2] = 16 => not allowed it will throw an error
print(tup)
"""

tup2 = ()
print(tup2)  # ()
print(type(tup2))  # <class 'tuple'>

# To create a single value tuple we will use (,) if we didnt used comma it will become integer -:
tup3 = (1,)
print(tup3)
print(type(tup3))

# Slicing in tuple -:

tup4 = (1, 2, 3, 4, 5)
tup4 = tup4[1 : len(tup4)]
print(tup4)

# Tuple methods -:

tup5 = (1, 2, 3, 4, 5, 6, 4, 7)
print(tup5.index(4))  # returns index of first ocuurance
print(tup5.count(4))  # count total occurance
