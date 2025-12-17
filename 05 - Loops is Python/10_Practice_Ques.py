print("Wap to find the sum of first n numbers using for loop")

n = int(input("Enter a number: "))
sum = 0
for i in range (1 , n + 1):
    sum += i
print("Total sum = ", sum)



print("Wap to find the sum of first n numbers using while loop")

n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print("Total sum =", sum)
 


print("Wap to find the factorial of first n numbers using for loop")
 
n = int(input("Enter a number: "))
product = 1
for i in range(1, n + 1):    
    product *= i

print(product)



print("Wap to find the factorial of first n numbers using while loop")
 
n = int(input("Enter a number: "))
product = 1
i = 1
while i <= n:
    product *= i
    i += 1
print(product)    