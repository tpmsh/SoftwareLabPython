class Year:
    def __init__(self,year):
        self.y = year
    def isLeap(self):
        y = self.y
        if((y%400 == 0) or ((y%4 == 0) and (y%100 != 0))):
            print("Leap ", end = "Year")
        else:
            print("Not Leap ", end = "Year")

year = int(input("Enter a Number :"))
Y = Year(year)
Y.isLeap()
