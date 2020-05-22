class Term:
    def __init__(self, coef = None, expo = None):
        self.coef = coef
        self.expo = expo
class Poly:
    def __init__(self):
        self.poly = []
    def addTerm(self,coef,expo = 0):
        if(coef != 0):
            term = Term(coef,expo)
            self.poly.append(term)

p = Poly()
p.addTerm(7.2,3)

print(p.poly[0].coef,p.poly[0].expo,sep = ' x^ ', end = ' + ')
