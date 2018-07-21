# Code being referenced from trevor payne youtube channel

# Traditional creation of a class with attribute
class MyClass(object):
    def __init__(self):
        self.x = 5

# TypeClass method in just 1 line of code
TypeClass = type('TypeClass', (object,), {'x':5})

m = MyClass()    # 5
t = TypeClass()    # 5

print(m.x, t.x)

# Creating TypeClass with functions
def printHam(self):
    print('ham')

TypeClass = type('TypeClass', (object,), {'x':5, 'pH':printHam})

t = TypeClass()
t.pH()