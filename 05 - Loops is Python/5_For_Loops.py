print(
    "For loops are used for sequential traversal. For traversing list, string, tuple etc"
)
"""
for loops 
for el in list:
    # some work 

for loop with else 
for el in list 
    # some work 
else:
    # work when loop ends
        
"""


print("accesing list elements using while loop")
list1 = [1, 2, 3, 4, 5]
idx = 0
while idx < len(list1):
    print(list1[idx])
    idx += 1


print("accesing list elements using For loop")
list2 = [5, 4, 3, 2, 1]
for val in list2:
    print(val)


print("accesing tuple elements using For loop")
tup1 = (1, 2, 3, 4, 5)
for val in tup1:
    print(val)


print("accesing str char using For loop")
str1 = "dev shraff"
for char in str1:
    print(char)


print("Break in for loop")
str2 = "syncdecodes"
for char in str2:
    if (char == "d"):
        print(char, "- d found")
        break
    print(char)
