list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)

list1.append(10) # appends elemnt at the last
print(list1)

list1.insert(2, 2.5)  # list.insert(index, element)
print(list1)





list2 = [92, 14, 45, 91, 2, 8, 7, 4, 0]
print(list2)

list2.sort() # sorts in ascending order
print(list2)

list2.sort(reverse= True) # sorts in descending order
print(list2)





list3 = [1, 2, 3, 4, 5, 1, 2]
list3.remove(2) # removes "first" occurence of element
print(list3)

list3.insert(1, 2)
print(list3)

list3.pop(6)
list3.pop(5)
print(list3)


fruits = ["Banana", "Water melon", "Apple", "Kiwi"]

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

