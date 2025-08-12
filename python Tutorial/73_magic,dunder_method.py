class Employee:
    name = 'Yash'

    def __len__(self):
        # The __len__ method is used to get the length of an object.
        i = 0
        for x in self.name:
            i = i + 1
        return i

    # The str and repr methods are both used to convert an object to a string representation.
    def __str__(self):
        return f"The name of the Employee is {self.name}"

    def __repr__(self):
        return f"Employee is {self.name}"

    def __call__(self, *args, **kwargs):
        return f"Employee is {self.name}"

emp = Employee()
print(emp)
print(str(emp))
print(repr(emp))
# print(emp.name)
# print(len(emp))
