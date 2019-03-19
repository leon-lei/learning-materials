from contextlib import contextmanager, suppress

################### Suppress ###################
# bad, just passing when handling ValueError
def print_float(x):
    try:
        print(float(x))
    except ValueError:
        pass

# good, shorter function with context manager
def print_float_cm(x):
    with suppress(ValueError):
        print(float(x))

print_float_cm(5)
print_float_cm('hello')


################### Create your own context manager ###################
class MyContextManager:
    def __enter__(self):
        print('Enter')
    
    def __exit__(self, *exc):
        print('Exit')


with MyContextManager():
    print('Inside the block!')


################### Context manager with as ###################
class FoodContextManager:
    def __init__(self):
        self.data = {}

    def __enter__(self):
        print(f'Enter: {self.data}')
        return self.data

    def __exit__(self, *exc):
        print(f'Exit: {self.data}')


with FoodContextManager() as data:
    data['fruit'] = 'delicious'


# using init
class FoodContextManager2:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        print(f'Enter: {self.data}')
        return self.data

    def __exit__(self, *exc):
        print(f'Exit: {self.data}')


with FoodContextManager2({'dairy': 'yuck'}) as data:
    data['fruit'] = 'delicious'


################### Context manager decorator ###################
# decorator creates the enter and exit for you
# yield is required
@contextmanager
def my_context_manager():
    print('Enter circle')
    yield
    print('Exit circle')

with my_context_manager():
    print('Inside the circle')


# rewrite earlier example
# must re-raise exceptions
@contextmanager
def FoodContextManager3(data):
    print(f'Enter {data}')
    yield data
    print(f'Exit {data}')

with FoodContextManager3({'dairy': 'yuck'}) as data:
    data['fruit'] = 'delicious'


################### Exceptions in __exit__ ###################
# do not re-raise exceptions in __exit__ methods 
class MyContextManager2:
    
    def __exit__(self, exc_type, exc, exc_tb):
        if exc:
            print('oh no!')
            call_for_help()
            # return False    # happens implicitly


# class ignores exceptions specified in init method
class suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc, exc_tb):
        return (
            exc_type is not None and issubclass(exc_type, self.exceptions)
        )