# Code being referenced from trevor payne youtube channel

def singleton(myClass):
    instances = {}
    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstance

@singleton
class TestClass(object):
    pass

x = TestClass()