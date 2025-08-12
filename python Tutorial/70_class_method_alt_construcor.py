class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_str(cls, sting):
        return cls(sting.split("-")[0], int(sting.split("-")[1]))


e1 = Employee("Ash", 15000)
print(e1.name)
print(e1.salary)

string = "Yash-15000"
e2 = Employee.from_str(string)
print(e2.name)
print(e2.salary)
