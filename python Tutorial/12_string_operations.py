games = "chess"
l = len(games)
print(l)
print(games[0:4])  # prints from 0 to n-1 (4-1 = 3)
print(games[1:4])
print(games[:4])
print(games[:])
print(games[:-3])  # or it can be written as
print(games[:len(games) - 3])
print(games[-3:-1])  # len - 3 : len - 1 = 5-3 : 5-1 = 2:4
print(games[-4:-2])
