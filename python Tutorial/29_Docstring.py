import this


def square(n):
    # This is a docstring which is just after function definition
    '''Takes in a number n, returns the square of n'''
    print(n ** 2)


square(5)
print(square.__doc__)
# Whenever string literals are present just after the definition of a function, module, class or method,
# they are associated with the object as their doc attribute.
# We can later use this attribute to retrieve this docstring.
