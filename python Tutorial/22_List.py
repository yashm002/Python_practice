# list comprehension
lst = [i * i for i in range(10)]
print(lst)

lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)

l1 = list('hello')
print(l1)

# creating list of single characters
l2 = list(input("Enter list elements: "))
print(l2)  # Data type is string to get actual datatype use eval function

# eval works for all data types and returns output of same datatype
l3 = eval(input("Enter list elements: "))
print(l3)
