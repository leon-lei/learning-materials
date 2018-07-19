# Code being referenced from trevor payne youtube channel

class MySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 10
        return self._instance

x = MySingleton()
print(x.y)

# Reassigning variable y
x.y = 35

z = MySingleton()
print(z.y)

foo = MySingleton()
print(foo.y)