print("Set is the collection of the 'unordered' items \n Each element in the set must be unique & immutable")
print("Sets can store values like Boolean, str, Int, Float and Tuple - list and dict cant be stored bcs they are mutable ")
print("Note that sets are mutable but the elements inside sets are immutable(cant be changed)")
print("Hashable value = Immutable value & Unhashable value = Mutable value")

set1 = {1, 2, 3, 4, 5, 2, 3,}
print(set1) # repeated elements stored only once, so it resolved to {1, 2, 3, 4, 5,}
print(type(set1)) # <class 'set'>

