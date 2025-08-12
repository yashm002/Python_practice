class Employee:
    companyName = "Apple"  # class variable
    noOfEmployees = 0

    def __init__(self, name):
        self.name = name  # instance variable
        self.raise_amount = 0.2
        Employee.noOfEmployees += 1

    def showdetails(self):
        print(f"The name of employee is {self.name} from {self.noOfEmployees} sized "
              f"company {self.companyName} and the raise amount is {self.raise_amount}.")


emp1 = Employee("Jay")
emp1.raise_amount = 0.5

# instance variable (first instance variable is checked if not found then class variable is used.
emp1.companyName = "Apple India"
emp1.showdetails()
# Employee.showDetails(emp1)

emp2 = Employee("Ankita")
emp2.showdetails()
