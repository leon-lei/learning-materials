# Original code from Dan Bader Real Python Youtube channel
# Modified namedtuple parameters
import collections
import multiprocessing
import os
import time
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'born',
])

scientists = (
    Scientist(name='alpha', born=1991),
    Scientist(name='beta', born=1978),
    Scientist(name='gamma', born=1998),
    Scientist(name='delta', born=2013),
    Scientist(name='epsilon', born=1987),
)

print(scientists, '\n')

def transform(x):
    print(f'Processing {os.getpid()} working record {x.name}')
    time.sleep(2)
    result = {'name': x.name, 'age': 2019 - x.born}
    print(f'Process {os.getpid()} done processing record {x.name}')
    return result

start = time.time()

pool = multiprocessing.Pool()    # spawns as many processes as machine's cpu cores
# pool = multiprocessing.Pool(processes=2)    # specifying set number of processes
# pool = multiprocessing.Pool(processes=len(scientists))    # dynamic
result =  pool.map(transform, scientists)

end = time.time()
print(f'\nTime to complete: {end - start:.2f}s\n')
pprint(result)
