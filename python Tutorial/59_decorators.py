def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thank you.")
    return mfx

@greet
def hello():
    print("Hello World")
hello()

# or it can be written as
# def hello():
#     print("Hello World")
# greet(hello)()

@greet
def add(a,b):
    print(a + b)
add(5,10)
