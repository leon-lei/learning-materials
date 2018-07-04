from collections import Counter

foo = [1,1,2,3,3,3,3,4]

counts = Counter(foo)

# Dict subclass so k,v pairs ordered by highest frequency
print(counts)    # Counter({3: 4, 1: 2, 2: 1, 4: 1})

# List n most common elements and their count in tuple form
# Indexing possible, returns tuple
print(counts.most_common(2))
print(counts.most_common(2)[0])    # (3, 4)
print(counts.most_common(2)[0][0])    # 3

# Get number of occurrences of an element
specific = counts[1]
print(specific)    # 2

# Nonexistant element does not return KeyError like standard dict
nonexist = counts[99]
print(nonexist)    # 0

# Redefine an element's count
counts[1] = 10
print(counts)    # Counter({1: 10, 3: 4, 2: 1, 4: 1})

# Pseudo delete where you set an element's count to 0
counts[1] = 0
print(counts)    # Counter({3: 4, 2: 1, 4: 1, 1: 0})

# Real delete
del counts[1]
print(counts)

# Convert to list, returns an ordered list
x = list(counts.elements())
print(x)    # [2, 3, 3, 3, 3, 4]

# Combine Counters
bar = [1,1,2,3,6,9,9]
counts2 = Counter(bar)
print(counts2)    # Counter({1: 2, 9: 2, 2: 1, 3: 1, 6: 1})
print(counts + counts2)    # Counter({3: 5, 2: 2, 1: 2, 9: 2, 4: 1, 6: 1})

# Subtract Counters
# Elements are removed from list if results were 0 or < 0
print(counts - counts2)    # Counter({3: 3, 4: 1})