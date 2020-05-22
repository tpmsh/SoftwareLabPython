class Prime:
    def __init__(self, num):
        self.num = num

    def isPrime(self):
        flag = True
        if(self.num > 1):
            for i in range(2,self.num//2,1):
                if(self.num % i == 0):
                    flag = False
                    return("Not Prime")

            if(flag):
                return("Prime")
        else:
            return("Less than One")

num = int(input("Enter a Number"))
P = Prime(num)
print("Number is "+P.isPrime())
