s1 = {1,2,4,5,8}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

# cities.intersection_update(cities2)
# print(cities)

cities3 = cities.symmetric_difference(cities2)
print(cities3)

# cities.symmetric_difference_update(cities2)
# print(cities)

cities3 = cities.difference(cities2)
print(cities3)

print(cities.isdisjoint(cities2))

cities3 = {"Delhi", "Madrid","Tokyo"}
print(cities.issuperset(cities2))
print(cities.issuperset(cities3))

print(cities3.issubset(cities))

cities.add("NYC") # To add multiple elements use update()
print(cities)

cities.remove("NYC")
# cities.discard("NYC") # remove and discard are same the diff is remove raises and error when element not found.
print(cities)

# del and clear()
# del cities

cities.clear()
print(cities)
