print("Understanding if - elif - else (syntax)")

age = int(input("Enter your age: "))
if age > 18:
    print("You are egligeble for driving")
else:
    print("You are not egligeble for driving")

num = int(input("Enter a number"))
if num == 20:
    print("Entered number is equal to 20")
elif num > 20:
    print("Entered number is greater than 20")

num1 = 5

if num1 > 2:
    print("Number is greter than 2")
if num1 > 3:
    print("Number is greater than 3")
    # both the conditions are True so both will get printed

    num2 = 10
    if num2 > 5:
        print("Number is greter than 5")
    elif num2 > 9:
        print("Number is greater than 9")
        # both the conditions are True but only if statement will get printed bcs here we used elif


# to Format python code type - black . and enter in terminal
#             or simply -:
# shift + alt + f
