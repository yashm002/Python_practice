lst = [1, 4, 6, 8, 22, 999, 299]

print(len(lst))
print(lst.index(22))

lst.append(300)
print(lst)

lst2 = [399, 499, 288]
lst.extend(lst2)
print(lst)

lst.insert(4, 55)
print(lst)

lst.pop()
print(lst)

# remove is used when we dk the index and it removes the first occurrence of a number
lst.remove(55)
print(lst)

ct = lst.count(8)
print(ct)

lst.sort()
print(lst)

# here s is a new list
s = sorted(lst2)
print(s)

lst.reverse()
print(lst)

print(min(lst))
print(max(lst))
print(sum(lst))

lst.clear()
print(lst)