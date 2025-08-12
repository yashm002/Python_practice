x = int(input("enter vlaue: "))

match x:
    case 0:
        print("value is 0")
    case 1:
        print("value is 1")
    case _x:
        print("value is",x)
