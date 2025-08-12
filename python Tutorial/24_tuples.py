tup = (1)  # type int
print(type(tup), tup)

tup = (1,)  # type tuple
print(type(tup), tup)

tup = (1,2,6,"kira",9,11,23,True,66,)
print(type(tup), tup)

# tuples are immutable
# tup[3] = 8
# print(tup)

tup2 = tup[1:5]
print(type(tup2), tup2)
