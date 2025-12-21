print(
    "Recursion - when a function call itself repeatedly \nnote that Recursion and loops are inter related"
)

print("Using Loop to print n to 1 backwards")


def show2(n2):
    for i in range(n2, 0, -1):
        print(i)


show2(5)


print("Using Recursion to print n to 1 backwards")


def show3(n3):
    if n3 == 0:  # Base case - means a condition where the loop should stop
        return
    print(n3)
    show3(n3 - 1)


show3(5)


print("Factorial using loop")


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(fact)


factorial(4)


print("Factorial using recursion")


def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return fact(n - 1) * n

print(fact(7))