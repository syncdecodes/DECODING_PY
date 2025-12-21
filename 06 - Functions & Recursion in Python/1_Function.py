print("Function is a block of statement that perform a specific task")
print("Basic syntax of a function -:")
"""
def func_name (param1, param2):
     some work 
    return val 

func_name(arg1, arg2)  function call
"""


# function definition 1 -:
print(("Product function"))


def product(a, b):
    return a * b


print(product(5, 4))


# function definition 2-:
print("Sum function")


def sum(a, b):
    sum = a + b
    return sum


result = sum(5, 5)
print(result)


# function definition 3 -:
print("Average of 3 numbers -:")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))


def average(a, b, c):
    return (a + b + c) / 3


print(average(num1, num2, num3))
