print("Ques 1 - print number from 1 to 50")
for i in range(1, 26):
    print(i)


print("Ques 2 - print number from 50 to 1")
for i in range(25, 0, -1):
    print(i)


print("Ques 3 - Multiplication table of number n")

n = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
