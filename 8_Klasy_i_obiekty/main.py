class Czytelnik:
    def __init__(self,name,surname,email,book) -> None:
        self.name=name
        self.surname=surname
        self.email=email
        self.book=book
        
        
    def __str__(self):
        return ({self.name},{self.surname}, {self.email}, {self.book})

C1 = Czytelnik("Julia", "Pietrak", "j.pietrak@gmail.com","Szklany Tron")
C2 = Czytelnik("Julia", "Gorzkiewicz", "j.gorzkiewicz@gmail.com","Zrodzeni z legendy")
C3 = Czytelnik("Joanna", "Jendrych", "jjendrych@gmail.com","Drobnym drukiem")

print(C1.__str__())
print(C2.__str__())
print(C3.__str__())