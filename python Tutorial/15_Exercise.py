import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

timestamp1 = int(time.strftime("%H"))
print(timestamp1)

if(timestamp1 >= 00 and timestamp1 < 12):
    print("Good morning sir")
elif(timestamp1 >= 12 and timestamp1 < 17):
    print("Good afternoon sir")
elif(timestamp1 >= 17 and timestamp1 < 19):
    print("Good afternoon sir")
else:
    print("Good night sir")
