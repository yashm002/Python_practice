letter = "Hey my name is {1} and i am from {0}"
name = "Yash"
location = "Nagpur"
print(letter.format(name,location))
print(letter.format(location,name))

# fstring
print(f"Hey my name is {name} and i am from {location}")

print(f"Hey my name is {{name}} and i am from {{location}}")
