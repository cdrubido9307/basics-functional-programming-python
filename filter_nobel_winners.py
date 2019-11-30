from inmutable_data_structure import scientist
import pprint

nobel_winners = tuple(filter(lambda  x: x.nobel is True, scientist))

# before casting to tuple
# Tuple is not an iterator
"""
while True:
    try:
        print(next(nobel_winners))
    except StopIteration:
        break
"""

# Using list comprehension approach
winners_and_physicist = (x for x in scientist if x.nobel is True and x.field=='Physics')
for x in winners_and_physicist:
    print(x)