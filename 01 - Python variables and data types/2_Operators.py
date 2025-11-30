print("Type of operatotrs -:")

print("Arithmetic operators - (+, -, *, /, %, **)")
print("Relational/ Comaprison operators - (==, !=, >, <, >=, <=)")
print("Assignment operators (=, +=, -=, *=, /=, %=, **=)")
print("Logic operators (not, and, or) ")



a = 5 
b = 2 
print (a ** b) # means a^b = 5^2 = 25
print (a == b) # False 
print (a != b) # True
# Relational operators returns boolean as an output means True or False



num = 10 
num = num + 10 
print (num) # 20

num2 = 10 
num2 += 10
print(num2) # 20




print(not False) # True
print(not True) # False

x = 10 
y = 10 
print (x is not y) # False
print (x is y) # True

j = 10 
k = 5
print(not (j > k)) # j is greater than k so ans is True but not will return its opposite False
print(not (j < k)) # True

val1 = 100
val2 = 50 
print((val1 and val2 )> 40) # True 
print((val1 and val2)< 45) # False 

print((val1 or val2) == 100 ) # True 
print((x > y) or (j > k)) # True as x is not > y so it will return False but j is > k so True - Final ans - True


# // is integer division (also called floor division). It divides normally, but removes the decimal part.

"""
eg -:
5 // 2 = 2
7 // 3 = 2
9 // 2 = 4
10 // 3 = 3

"""
