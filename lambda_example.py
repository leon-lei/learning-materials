<<<<<<< HEAD
people = ['Dr. Ben Carver', 'Mr. Bill Sash', 'Mrs. Wendy Marvel', 'Mr. Mas Lill']

def split_title_last(person):
    return person.split()[0] + ' ' + person.split()[-1]

# option 1
for person in people:
    print(split_title_last(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# option 2
print(list(map(split_title_last, people,)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))
=======
people = ['Dr. Ben Carver', 'Mr. Bill Sash', 'Mrs. Wendy Marvel', 'Mr. Mas Lill']

def split_title_last(person):
    return person.split()[0] + ' ' + person.split()[-1]

# option 1
for person in people:
    print(split_title_last(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# option 2
print(list(map(split_title_last, people,)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))
>>>>>>> origin/master
