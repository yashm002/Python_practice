def average(*numbers):  # parameters
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average of numbers is: ", sum / len(numbers))

average(1, 4, 6, 9) # arguments

# def intrest(principal, time=2, rate=0.10):  # parameters (default)
#     si = (principal * rate * time) / 100
#     return si
#
#
# rs = intrest(10000, 5, 1)  # arguments
# print(rs)
