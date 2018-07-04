from collections import defaultdict

# First arg provides initial value for default_factory
# int() == 0
d = defaultdict(int)
d['jan'] += 5
print(d['feb'])    # value is 0 because of int default_factory, no KeyError
print(d['jan'])    # 5
print(d)    # defaultdict(<class 'int'>, {'jan': 5, 'feb': 0})

# Example with list
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k,v in s:
    d[k].append(v)

print(d)    # defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
print(sorted(d.items()))    # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])] 