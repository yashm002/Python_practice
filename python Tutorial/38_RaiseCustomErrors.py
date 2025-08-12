a = input("Enter any value between 5 and 9 : ")

if a == "quit":
    print("you choosed to quit")
elif (int(a) < 5 or int(a) > 9):
    raise ValueError("Value should be between 5 and 9")
else:
    print(a)