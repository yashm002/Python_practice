# a lambda function is a small anonymous function without a name it is defined using the lambda keyword.

# def double(x):
#     return x * 2

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(3))
print(avg(2, 5, 8))
