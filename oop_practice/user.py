from library import Base


assert hasattr(Base, 'foo'), 'foo does not exist in Base class'

class Derived(Base):
    def bar(self):
        return self.foo()