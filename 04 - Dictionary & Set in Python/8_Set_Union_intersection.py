set1 = {1, 2, 3 , 4, 5, 6, 7, 8, 9}
set2 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print(set1.union(set2)) # combines both set values and returns new
print(set1.intersection(set2)) # combines common values and returns new



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", ["none"])

print(x)
