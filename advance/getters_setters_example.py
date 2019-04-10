# Example code from Aaron Hall StackOverflow response
# https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters/36943813#36943813

class Protective(object):
    def __init__(self, start_protected_value=0):
        self.protected_value = start_protected_value

    @property
    def protected_value(self):
        return self._protected_value

    @protected_value.setter
    def protected_value(self, value):
        if value != int(value):
            raise TypeError("protected_value must be an integer")
        if 0 <= value <= 100:
            self._protected_value = int(value)
        else:
            raise ValueError("protected_value must be " +
                             "between 0 and 100 inclusive")

    @protected_value.deleter
    def protected_value(self):
        raise AttributeError("do not delete, protected_value can be set to 0")


foo = Protective()
foo.protected_value = 35
print(foo.__dict__)

foo.protected_value = 200 # raises ValueError
del foo.protected_value # raises AttributeError
