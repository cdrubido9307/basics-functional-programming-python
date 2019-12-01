from functools import reduce
from inmutable_data_structure import scientist
from map_demo import name_and_ages
import collections
from pprint import pprint

total_age = reduce(lambda  acc, val: acc + val['age'], name_and_ages, 0)
print(total_age)

by_field = {'Math': [], 'Physics': [], 'Chemistry': [], 'Astronomy': []}

def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

scientist_by_field = reduce(reducer, scientist, by_field)
print(scientist_by_field)

# Other way to do the same using defaultdict

sci_by_field = reduce(reducer, scientist, collections.defaultdict(list))
pprint(sci_by_field)