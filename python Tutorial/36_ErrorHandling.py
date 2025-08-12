# a = input("Enter a number: ")
# print(f"Multiplication table of {a} is: ")
#
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} : {int(a) * i}")
# except:
#     print("Invalid Input")

try:
    num = int(input("Enter a number: "))
    a = [5,2]
    print(a[num])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index error")