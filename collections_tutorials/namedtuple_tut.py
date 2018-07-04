from collections import namedtuple

# Similar to dict but tuples are immutable
# Good for preserving data and not modifying it

Color = namedtuple('Color', ['red', 'green', 'blue'])

# Kwargs work but not necessary
# foo = Color(red=35, green=32, blue=122)
foo = Color(35,32,122)

# Indexing possible but .attribute is more readable
print(foo[0])    #35
print(foo.red)    #35