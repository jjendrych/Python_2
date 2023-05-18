class Czytelnik:
    def __init__(self,reader_num,name,surname,email,book) -> None:
        self.__name=name
        self.__surname=surname
        self.__email=email
        self.__book=book
        self.__reader_num=reader_num
        
        
    def __str__(self):
        return (f"{self.__reader_num},{self.__name},{self.__surname}, {self.__email}, {self.__book}")
    
    def modifyReader(self):
        print("Dane, które możesz edytować")
        print("1.Numer czytelnika")
        print("2.Imię")
        print("3.Nazwisko")
        print("4.Wypożyczona książka")
        choice = input("Które dane chcesz edytować?:")
        if choice == "1":
            new_reader_num = input("Nowy numer czytelnika: ")
            self.__reader_num = new_reader_num
        elif choice == "2":
            new_name = input("Nowe imię: ")
            self.__name = new_name
        elif choice == "3":
            new_surname = input("Nowe nazwisko: ")
            self.__surname = new_surname
        elif choice == "4":
            new_book = input("Nowa wypożyczona książka: ")
            self.__book = new_book
        else:
            print("Nieprawidłowy wybór")
            
    def __deleteReader__(self):
        del self
    
    def sayHello(self):
        print("Witaj "+self.__name+" !. Miło mi cię poznać")
              
    
C1 = Czytelnik("12153","Julia", "Pietrak", "j.pietrak@gmail.com","Szklany Tron")
C2 = Czytelnik("78546","Julia", "Gorzkiewicz", "j.gorzkiewicz@gmail.com","Zrodzeni z legendy")
C3 = Czytelnik("45452","Joanna", "Jendrych", "jjendrych@gmail.com","Drobnym drukiem")

print(C1.__str__())
print(C2.__str__())
print(C3.__str__())

C1.modifyReader()
print(C1.__str__())

C2.sayHello()

