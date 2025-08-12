class Person:
    # When the constructor accepts arguments along with self, it is known as parameterized constructor.
    def __init__(self, name, occ):
        print("Hey i am person")
        self.name = name
        self.occupation = occ

    # When the constructor doesn't accept any arguments from the object and
    # has only one argument, self, in the constructor, it is known as a Default constructor.
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person("Yash", "HR")
b = Person("Jay", "Designer")
a.info()
b.info()
