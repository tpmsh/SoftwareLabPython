class Fibo:
    def __init__(self, nTerms):
        self.nTerms = nTerms
    def fibo(self):
        nTerms = self.nTerms
        first = 0
        second = 1
        print("0, 1, ",end = '')
        for i in range(nTerms):
            third = first + second
            print(third, end = ', ')
            first = second
            second = third

num = int(input("Enter No. of Terms"))
F = Fibo(num)
F.fibo()
