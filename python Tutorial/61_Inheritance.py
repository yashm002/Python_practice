class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee with id {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python.")


emp1 = Employee("Pranav", 220)
emp1.showDetails()

emp2 = Programmer("Vinod", 250)
emp2.showDetails()
emp2.showLanguage()
