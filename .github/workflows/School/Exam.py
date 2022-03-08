def makeDecorator(func):
    def decorator():
        func()
        print("What comes first?")
    return decorator

@makeDecorator
def a():
    print("chicken")

@makeDecorator
def b():
    print("egg")

a()