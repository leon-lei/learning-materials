# Code being referenced from trevor payne youtube channel

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, *kwargs)
            cls.x = 5
        return cls._instances[cls]

# When class is defined, python searches for a metaclass definition
# At the time of this creation, Singleton method ensures only 1 of the class
# is created
class MyClass(metaclass=Singleton):
    pass

# Multiple instances at different variables are all pointing towards the same instance
m = MyClass()
v = MyClass()
print(m.x)
m.x = 9
print(v.x)