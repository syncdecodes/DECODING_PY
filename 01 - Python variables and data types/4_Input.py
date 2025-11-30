value = input("Enter some value: ")
print(value,"you entered:", type(value)) # input always converts value into string 


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
sum = num1 + num2 
print (sum)


side = float(input("Enter side of square: "))
Area = side * side 
print ("The Area of the side of the square is: ", Area,"cm^2" )


num3 = float(input("Enter a decimal number: "))
num4 = float(input("Enter another decimal number: "))
average = (num3 + num4) / 2 
print("the average of",num3, "and", num4, "is", average)


a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print((a > b) or (a == b))