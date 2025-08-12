# strings are immutable
# while we perform operations on string real string does not change, a new string is created.

name = 'My name is Yash!'
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace('Yash', 'Raj'))
print(name.count('Yash'))
print(name.split())
print(name.center(30))
print(name.endswith("!"))
print(name.startswith('name'))
print(name.find('is'))  # returns -1 if sub string is not found
print(name.index('name'))  # similar to find, the diff is it raises an error when sub string is not found
print("\n")

name2 = '***Yash***'
print(name2)
print(name2.lstrip('*'))
print(name2.rstrip('*'))
print(name2.strip('*'))
print("\n")

name3 = 'Helloash'
print(name3.isalnum())
print(name3.isalpha())
print(name3.isspace())
print(name3.istitle())
print(name3.title())
print("\n")

name4 = "hey guys\n"
print(name4.isprintable())
