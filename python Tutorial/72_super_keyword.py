class Employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


ash = Employee(403, "Ash")
yash = Programmer("yash", 499, "python")
print(yash.name)
print(yash.id)
print(yash.lang)
