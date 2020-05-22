class Factorial:
    def __init__(self,num):
        self.num = num
        self.fact = 1

    def factorial(self):
        for i in range(1,num + 1,1):
            self.fact = self.fact * i
        return self.fact

num = int(input("Enter a Number : "))
f = Factorial(num)
print("Factorial of " + str(num) + " is " + str(f.factorial()))
