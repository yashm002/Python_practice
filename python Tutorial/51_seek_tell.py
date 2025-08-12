# The seek() function allows you to move the current position within a file to a specific point.
# The tell() function returns the current position within the file, in bytes.

# with open('myfile.txt', 'r') as f:
#     # Move to the 10th byte in the file
#     f.seek(10)
#
#     # Read the next 5 bytes
#     data = f.read(5)
#     print(data)

with open('myfile.txt', 'r') as f:
    f.seek(10)
    print(f.tell())

    data = f.read(5)
    print(data)

with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())
