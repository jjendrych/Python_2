import json
import os
"""Klasa trzymająca wszelkie metody związane z plikiem json"""
class jsonOperations():
    def __init__(self) -> None:
        self.data = self.showJson()
        
    def saveToJson(self):
        """Automatyczny zapis wszelkich zadań do pliku json"""
        with open('todolist.json', 'w') as file:
            json.dump(self.data, file)

    def showJson(self):
        """Wyświetlanie zawartości pliku json"""
        if os.path.exists('todolist.json') and os.stat('todolist.json').st_size > 0:
            with open('todolist.json') as file:
                data = json.load(file)
                return data
        else:
            return []
        
"""Klasa ma metody odpowiadające wszystkim podstawowym elementom programu todo listy jak dodanie zadania, usunięcie lub zmodyfikowanie go"""        
class generalOperations(jsonOperations):
    def showTasks(self):
        """Funkcja wyświetlająca zapisane zadania"""
        if not self.data:
            print("Lista todo jest pusta.")
        else:
            print("\nZadania:")
            for task in self.data:
                print(f"ID: {task['id']}")
                print(f"Tytuł zadania: {task['title']}")
                if 'description' in task:
                    print(f"Opis zadania: {task['description']}")
                print(f"Data wykonania zadania: {task['task_deadline']}")
                print()

    def addTask(self):
        """Funkcja dodająca zadanie. Pozwala użytkownikowi na wprowadzenie tytułu, opisu i daty wykonania zadania"""
        title = input("Wprowadź tytuł zadania:")
        if title == "":
            print("Nie można dodać zadania bez tytułu")
        else:
            """Możliwość wyboru istnienia opisu zadania"""
            desc=input("Czy chcesz dodać opis zadania? (wpisz tak lub nie): ")
            if desc in ['Tak','tak', 't','T']:
                description = input("Opisz zadanie do wykonania:")
            else:
                description=None
                
            print("Wprowadź dane dotyczące daty wykonania zadania:")
            day = input("Dzień: ")
            month = input("Miesiąc: ")
            year = input("Rok: ")
            task_deadline = f"{day}-{month}-{year}"
            
            if self.data:
                last_id = self.data[-1]['id']
                new_id = last_id + 1
            else:
                new_id = 1

            task = {
                "id": new_id,
                "title": title,
                "task_deadline": task_deadline
            }
            if description:
                task['description'] = description
                    
            self.data.append(task)
            self.saveToJson()
            print("Zadanie zostało dodane!")
                
    def deadline(self) -> str:
        """Funkcja umożliwiająca użytkownikowi wprowadzenie daty zadania"""
        print("Wprowadź dane dotyczące daty wykonania zadania:")

        day = input("Dzień: ")
        month = input("Miesiąc: ")
        year = input("Rok: ")

        if day.isdigit() and month.isdigit() and year.isdigit() and 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
            task_deadline = f"{int(day)}-{int(month)}-{int(year)}"
            return task_deadline

        print("Wprowadzono nieprawidłowe dane. Proszę spróbować ponownie.")
            
    def deleteTask(self):
        """Funkcja usuwająca zadanie"""
        self.showTasks()
        remove_this_id = int(input("Podaj numer zadania, które chcesz usunąć: "))
        for task in self.data:
            if task['id'] == remove_this_id:
                self.data.remove(task)
                self.saveToJson()
                print("Zadanie zostało usunięte.")
                return
        print("Nie znaleziono zadania o podanym ID.")
        
    def modifyTask(self):
        """Funckja modyfikująca dane wybranego zadania. Dane zadania są zamieniane na te wprowadzone przez użytkownika"""
        if not self.data:
            print("Nie masz żadnych zadań do edycji.")
        else:
            self.showTasks()
            modify_this_id=int(input("Podaj numer zadania, które chcesz edytować: "))
            for task in self.data:
                if task['id'] == modify_this_id:
                    print("Możliwe dane do modyfikacji:")
                    print("1. Tytuł")
                    if 'description' in  task:
                        print("2. Opis zadania")
                        print("3. Data wykonania zadania")
                        choice = input("Którą daną zadania chcesz edytować?: ")

                        if choice == "1":
                            new_title = input("Podaj nowy tytuł zadania: ")
                            task['title'] = new_title
                            save = input("Czy chcesz aby zmiana zostały zapisana? (wpisz tak lub nie): ")
                            """Upewnienie się czy użytkownik na pewno chce zapisać zmiany zadania"""
                            if save in ['tak', 'Tak', 't','T']:
                                self.saveToJson()
                                print(f"Tytuł zadania {modify_this_id} został zaaktualizowany. Nowy opis to: {new_title}")
                                return
                            else:
                                print("Zmiany nie zostały zapisane!")
                                return

                        elif choice == "2" and 'description' in task:
                            new_description = input("Podaj nowy opis zadania: ")
                            task['description'] = new_description
                            save = input("Czy chcesz aby zmiana zostały zapisana? (wpisz tak lub nie): ")
                            """Upewnienie się czy użytkownik na pewno chce zapisać zmiany zadania"""
                            if save in ['tak', 'Tak', 't','T']:
                                self.saveToJson()
                                print(f"Opis zadania {modify_this_id} został zaaktualizowany. Nowy opis to: {new_description}")
                                return
                            else:
                                print("Zmiany nie zostały zapisane!")
                                return

                        elif choice == "3":
                            new_deadline = self.deadline()
                            task['task_deadline'] = new_deadline
                            save = input("Czy chcesz aby zmiana zostały zapisana? (wpisz tak lub nie): ")
                            """Upewnienie się czy użytkownik na pewno chce zapisać zmiany zadania"""
                            if save in ['tak', 'Tak', 't','T']:
                                self.saveToJson()
                                print(f"Data zadania {modify_this_id} została zaaktualizowana. Nowy opis to: {new_deadline}")
                                return
                            else:
                                print("Zmiany nie zostały zapisane!")
                                return
                    
                    else:
                        print("2. Data")
                        choice = input("Którą daną zadania chcesz edytować?: ")

                        if choice == "1":
                            new_title = input("Podaj nowy tytuł zadania: ")
                            task['title'] = new_title
                            save = input("Czy chcesz aby zmiana zostały zapisana? (wpisz tak lub nie): ")
                            """Upewnienie się czy użytkownik na pewno chce zapisać zmiany zadania"""
                            if save in ['tak', 'Tak', 't','T']:
                                self.saveToJson()
                                print(f"Tytuł zadania {modify_this_id} został zaaktualizowany. Nowy opis to: {new_title}")
                                return
                            else:
                                print("Zmiany nie zostały zapisane!")
                                return

                        elif choice == "2":
                            new_deadline = self.deadline()
                            task['task_deadline'] = new_deadline
                            save = input("Czy chcesz aby zmiana zostały zapisana? (wpisz tak lub nie): ")
                            """Upewnienie się czy użytkownik na pewno chce zapisać zmiany zadania"""
                            if save in ['tak', 'Tak', 't','T']:
                                self.saveToJson()
                                print(f"Data zadania {modify_this_id} została zaaktualizowana. Nowy opis to: {new_deadline}")
                                return
                            else:
                                print("Zmiany nie zostały zapisane!")
                                return

            print("Nie znaleziono zadania o podanym ID.")
    
"""Klasa pozwalająca podjęcie na podjęcie działań, które użytkownik sam wybierze z menu"""
class ToDoList(generalOperations):
    def menu(self) -> str:
        """Wyświetlenie uzytkownikowi dostępnych opcji w todo liście"""
        print("\nMenu:")
        print("1.Dodaj zadanie")
        print("2.Usuń zadanie")
        print("3.Aktualizuj zadanie")
        print("4.Zapisz plik z zadaniami")
        print("5.Wyświetl wszystkie zadania")
        print("0.Wyjście z todo list")
        choice = input("Wybierz opcję:")
        return choice
            
    def main(self):
        self.showTasks()
        while True:
            choice = self.menu()

            if choice == "1":
                self.addTask()
                self.showJson()

            elif choice == "2":
                self.deleteTask()
                self.showJson()

            elif choice == "3":
                print("Zadania, które możesz zaktualizować:")
                self.showJson()
                self.modifyTask()

            elif choice == "4":
                self.saveToJson()
                print("Zadania zostały zapisane!")
            
            elif choice == "5":
                self.showTasks()

            elif choice == "0":
                self.saveToJson()
                print("Dziękuję za skorzystanie z todo listy! Powodzenia w wykonywaniu swoich zadań!")
                break

            else:
                print("Nie ma takiej opcji. Proszę wybrać jedną z dostępnych opcji")


todo_list = ToDoList()
todo_list.main()