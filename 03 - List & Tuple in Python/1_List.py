print("Just like arrays in JS there is list in python")
marks = [96, 94, 98, 74, 30, 28, 80, 43, 98]
print (marks)
print(type(marks)) # <class 'list'>
print(len(marks))
print (marks[1]) # 94
print (marks[5]) # 28

print("In python we can store elements of different types (integers, float, string, etc..) in the list")

student = ["Dev", 17, "Delhi", "KMV", 81.96, True, None]
print(student)

print("Just like JS in python strings are also immutable (which can't be changed) and list are mutable (which can be changed)")

"""
example -:
str1 = "Hello world"
str1[0] = "P"
print(str1)  error bcs strings are immutable
"""

list1 = ["syncdecodes", 9]
list1[0] = "Dev codes"
print(list1) # ['Dev codes', 9]

