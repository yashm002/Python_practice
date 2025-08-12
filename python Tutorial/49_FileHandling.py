# Reading a file
f = open("myfile.txt","r")
text = f.read()
print(text)
f.close()

# writing in a file
# f1 = open("myfile2.txt","w")
# f1.write("Hello ash!")
# f1.close()

# appending in a file
f2 = open("myfile2.txt","a")
f2.write("Hello yash!")
f2.close()

# using with u don't have to close the file
with open("myfile2.txt","a") as f2:
    f2.write("\nHey I am inside with...")