import collections
import concurrent.futures
import os
import time
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

scientist = (
    Scientist(name='Ada Lovelance', field='Math', born=1815, nobel=False),
    Scientist(name='Emmy Noethere', field='Math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='Physics', born=1867, nobel=True),
    Scientist(name='To Youyou', field='Chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='Chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='Astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='Physics', born=1951, nobel=False),
)

def transform(x):
    print(f'Process {os.getpid()} working on record {x.name}')
    time.sleep(2)
    result = {'name': x.name, 'age': 2019 - x.born}
    print(f'Process {os.getpid()} done processing {x.name}')
    return result

if __name__ =='__main__':
    pprint(scientist)
    print('__________________________________________________________________________')

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as ex:
        scientist_ages = tuple(ex.map(transform, scientist))

    # First try it without multiprocessing(uncoment bellow, comment above)
    # scientist_ages = tuple(map(transform, scientist))

    end_time = time.time()

    print(f'\nTime to complete: {end_time - start_time:.2f}s\n')
    pprint(scientist_ages)