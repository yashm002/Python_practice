# A class is a blueprint or a template for creating objects.
# Object is the instance of the class used to access the properties of the class.
class Person:  # Class
    name = "Yash"
    occupation = "Data Scientist"
    networth = 150

    # The self parameter is a reference to the current instance of the class, and
    # is used to access variables that belongs to the class.
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()  # Object
b = Person()
c = Person()

a.name = "Raj"
a.occupation = "Businessman"

b.name = "Harsh"
b.occupation = "Doctor"

a.info()
b.info()
c.info()
