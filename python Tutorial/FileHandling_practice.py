# read(), readline() and readlines() method

# f = open("myfile.txt")
# text = f.read()
# print(text)
# f.close()


# f = open("myfile.txt")
# text = f.read(50)
# print(text)
# f.close()

# f = open("myfile.txt")
# text = f.readline()
# print(text)
# f.close()

# f = open("myfile.txt")
# text = f.readline(3)
# print(text)
# f.close()

# f = open("myfile.txt")
# text = f.readlines()
# print(text)
# f.close()

# Reading a complete file line by line
f = open("myfile.txt")
str =" "
while str:
    str = f.readline()
    print(str,end='')
f.close()
