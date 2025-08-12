class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod  # with static method no need to pass default self argument
    def add(a, b):
        return a + b


m = Math(5)
print(m.num)

m.addtonum((5))
print(m.num)

print(m.add(5, 7))
