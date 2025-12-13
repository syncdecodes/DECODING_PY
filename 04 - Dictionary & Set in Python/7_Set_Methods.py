set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10}
print(set1)

set1.add("Ten") # .add - adds value at the last in the set
set1.add((11, 12, 13, 14, 15))
print(set1)

set1.remove(10) # removes the specific value
print(set1)

print(len(set1))

set1.pop() # removes a random value
print(set1)

set1.clear() # empties the whole set
print(set1)