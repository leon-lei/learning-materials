# Code being referenced from trevor payne youtube channel

# A factory is a Design Pattern that lets a function choose the class to return
# Type creation method
# Benefits:
# Allows creation of thing on the fly without explicit hard code
# Remvoes duplication of code within multiple classes

BaseClass = type("BaseClass", (object,), {})

@classmethod
def Check1(self, myStr):
    return myStr == 'ham'

@classmethod
def Check2(self, myStr):
    return myStr == 'sandwich'

C1 = type("C1", (BaseClass,), {"x":1, "Check":Check1})
C2 = type("C2", (BaseClass,), {"x":30, "Check":Check2})

def MyFactory(myStr):
    for cls in BaseClass.__subclasses__():
        if cls.Check(myStr):
            return cls()

m = MyFactory("ham")
v = MyFactory("sandwich")

print(m.x, v.x)