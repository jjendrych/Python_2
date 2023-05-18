class Quadrangle:    
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    
    def sides(self):
        print("Długość boków:")
        print("a= ", self.a)
        print("b= ",self.b)
        print("c= ",self.c)
        print("d= ",self.d)
        
    def area(self):
        pass
    
    def circum(self):
        pass
        
class Square(Quadrangle):
    def area(self):
        return self.a * self.a
    def circum(self):
        return (self.a*4)

class Rectangle(Quadrangle):
    def area(self):
        return self.a * self.b
    def circum(self):
        return (2*self.a + 2*self.b)

print("Dla której figury chcesz policzyć obwód i pole?")
print("1.Kwardat")
print("2.Prostokąt")
choice = int(input("Twój wybór: "))
if choice == 1:
    a= print("Podaj długość boku kwadratu: ")
    S = Square(a,a,a,a)
    print("-------- Obliczenia dla kwadratu----------")
    print("Długość poszczególnych boków:")
    S.sides()
    print("Pole kwadratu:", S.area())
    print("Obwód kwadratu: ", S.circum())
    
if choice == 2:
    a = int(input("Podaj długość pierwszego boku: "))
    b = int(input("Podaj długość drugiego boku: "))
    
    R = Rectangle(a,b,a,b)
    print("-------- Obliczenia dla prostokąta----------")
    print("Długość poszczególnych boków:")
    R.sides()
    print("Pole kwadratu:", R.area())
    print("Obwód kwadratu: ", R.circum())

    