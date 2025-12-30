# To make a priveate attribute or method private use __
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # now this is private and can be accessed publicly

    def reset_pass(self):
        return self.__acc_pass

acc1 = Account(1, 9876)
print(acc1.acc_no)
# print(acc1.__acc_pass) # AttributeError: 'Account' object has no attribute '__acc_pass'
print(acc1.reset_pass()) # no error

# eg 2 

class Person:
    __name = "anonymous"

    def __hello(self):
        return "hello"
    def welcome(self):
        return self.__hello()

p1 = Person()
# print(p1.__name) # AttributeError: 'Person' object has no attribute '__name'
# print(p1.__hello()) # AttributeError: 'Person' object has no attribute '__hello' 
print(p1.welcome())

# PRIVATE ATTRIBUTES AND METHODS ARE MEANT TO BE USED ONLY WITHIN THE CLASS AND ARE NOT ACCESSIBLE FROM OUTSIDE THE CLASS.
# AGAR HUMNE ATTRIBUTES YA METHODS KO DOUBLE UNDERSCORE ( __ ) SE PRIVATE BANA DIA TOH USE CLASS KE SIRF JO INTERNAL FUNCTION HAI WAHI ACCESS KAR PAENGE BAHAR KOI USE ACCESS NAHI KAR PAEGA.



