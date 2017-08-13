def simple_gen():
    yield 'Oh'
    yield 'Hello'
    yield 'There'

for i in simple_gen():
    print(i)

CORRECT_COMBO = (6, 1, 9)

# loop keeps running even after correct combo was found
for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo: {}'.format((c1,c2,c3)))
            print(c1, c2, c3)

# loop will stop after correct combo is found
# but you require multiple lines of codes to break at each level of the loop
found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo: {}'.format((c1,c2,c3)))
                found_combo = True
                break
            print(c1, c2, c3)

# now create a generator to yield the combo
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo: {}'.format((c1,c2,c3)))
        break
    print(c1, c2, c3)