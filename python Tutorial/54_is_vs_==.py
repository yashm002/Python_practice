p = [22, 44, 66]  # list is mutable
q = [22, 44, 66]

print(p is q)  # compares exact location of object in memory
print(p == q)  # compares values

a = 3  # constant is immutable
b = 3

print(a is b)  # compares exact location of object in memory
print(a == b)  # compares value
