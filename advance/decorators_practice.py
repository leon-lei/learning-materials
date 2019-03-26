# Code referenced from Sebastiaan Mathot YouTube tutorial
from functools import wraps


################################ Decorators without arguments ################################
def camelcase(s):
    """Turn strings_like_this into StringLikeThis"""
    return ''.join([word.capitalize() for word in s.split('_')])

print(camelcase('snoop_dogg'))  # returns 'SnoopDogg'

# In order to pass the list of names into camelcase function
# Decorate it with another function
def mapper(fnc):
    @wraps(fnc)
    def inner(list_of_values):
        """This is the inner()"""
        return [fnc(value) for value in list_of_values]
    return inner

@mapper
def camelcase2(s):
    """Turn strings_like_this into StringLikeThis"""
    return ''.join([word.capitalize() for word in s.split('_')])

names = [
    'rick_ross',
    'asap_rocky',
    'snoop_dogg',
]

print(camelcase2(names))    # returns ['RickRoss', 'AsapRocky', 'SnoopDogg']

# Thanks to wraps decorator, we can see the doc string of camelcase2() instead of the docstring from inner() 
print(camelcase2.__doc__)    # Turn strings_like_this into StringLikeThis


################################ Decorators with arguments ################################
# Requires a bit of nesting and "meta decorator"

def power_of(arg):
    def decorator(fnc):
        def inner():
            return fnc() ** exponent
        return inner
    
    if callable(arg):
        exponent = 2
        return decorator(arg)
    else:
        exponent = arg
        return decorator


@power_of
def always_two():
    return 2

@power_of(4)
def always_three():
    return 3

print(always_two())    # returns 4 for 2 to the power of 2 (default exponent when no arg is passed to decorator)
print(always_three())    # returns 81 for 3 to the power of 4

