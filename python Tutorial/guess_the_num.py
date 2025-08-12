import random

n = random.randint(0,20)
print(n)
i=1
while i<=5:
    g1=int(input("Guess the number: "))
    if(g1==n):
        print("You won!")
        break
    else:
        if(i<5):
            print("try again")
            i=i+1
        else:
            print("You lost the number was: ",n)
            break