# ploymorphism : operator overloading
# when the same operator is allowed to have different meaning according to the context

# print(1 + 2)  # 3
# print("dev" + "codes")  # concatenate => devcodes
# print([1, 2, 3] + [4, 5, 6])  # merge => [1, 2, 3, 4, 5, 6]


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def display(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(3, 4)
num1.display()

num2 = Complex(5, 6)
num2.display()

# num3 = num1.add(num2)
# num3.display()

num3 = num1 + num2
num3.display()
