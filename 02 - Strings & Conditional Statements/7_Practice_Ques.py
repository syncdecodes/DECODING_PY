num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

val1 = int(input("Enter 1st number: "))
val2 = int(input("Enter 2nd number: "))
val3 = int(input("Enter 3rd number: "))

if (val1 > val2) and (val2 > val3):
    print(val1, val2, val3, val1, "is greter than", val2, "and", val3)

elif (val2 > val1) and (val1 > val3):
    print(val1, val2, val3, val2, "is greter than", val1, "and", val3)

else:
    print(val1, val2, val3, val3, "is greter than", val1, "and", val2)


num2 = int(input("Enter a number: "))

if (num2 % 7) == 0:
    print(num2, "is a multiple of 7")
else:
    print(num2, "is not a multiple of 7")
