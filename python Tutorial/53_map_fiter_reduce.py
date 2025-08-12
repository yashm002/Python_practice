# MAP
def cube(x):
    return x*x*x

l = [1,2,4,5,6,2]

# newl = []
# for i in l:
#     newl.append(cube(i))
# print(newl)

# The map function applies a function to each element in a sequence and returns a new sequence containing the
# transformed elements
newl = list(map(cube,l))
print(newl)

# FILTER

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))

# REDUCE

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
