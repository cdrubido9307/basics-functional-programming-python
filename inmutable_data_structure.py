import collections

# Name Tuples are inmutable data structures
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
    Scientist(name='To Youyou', field='Chemistry', born=1939, nobel=True),
    Scientist(name='Ada Yonath', field='Chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='Astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='Physics', born=1951, nobel=False),
)