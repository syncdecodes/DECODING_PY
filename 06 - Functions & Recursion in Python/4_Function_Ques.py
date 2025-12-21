print("Ques 1 - waf to print the length of a list")


def length(a):
    length = len(a)
    print(length)


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
length(list1)


print("Ques 2 - waf to print the elements of a list in a single vertical line.")


def length2(x):
    print(x)
    length2 = len(x)
    for i in range(0, length2):
        print("idx", i, " - ", x[i])


list2 = ["apple", "banana", "kiwi", "orange", "guava"]
length2(list2)


print("Ques 3 - waf to print the elements of a list in a single horizontal line.")


def length3(x):
    length3 = len(x)
    print("Length of list is - ", length3)
    for item in x:
        print(item, end=", ")


list3 = [
    "apple",
    "banana",
    "kiwi",
    "orange",
    "guava",
    "grape",
    "dragon fruit",
    "papaya",
]
length3(list3)


print("Ques 4 - waf to find the factorial of n")


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)


factorial(5)


print("Ques 5 - waf to covert usd to INR")


def usd_inr(amt):
    print(amt * 88.17)


usd_inr(4)


print("Ques 6 - waf to covert INR to usd")


def inr_usd(amt):
    print(amt / 88.17)


inr_usd(100)


print("Ques 7 - waf to tell the user whether the entern number is even or odd")

def ev_odd(num):
    if(num % 2 == 0):
        print(num, "is EVEN")
    else:
        print(num, "is ODD")

ev_odd(8)        