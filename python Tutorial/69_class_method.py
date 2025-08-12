class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

    @classmethod
    def change_company(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Ash"
e1.show()
e1.change_company("Microsoft")
e1.show()
print(Employee.company)
