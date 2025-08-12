def func1():
    try:
        lst = [1, 4, 6, 7, 8]
        i = int(input("Enter index: "))
        print(lst[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("This is always executed")
    # print("This is always executed")


x = func1()
print(x)