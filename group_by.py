import itertools
from inmutable_data_structure import scientist
from pprint import pprint

scientist_by_field = {
    item[0]: list(item[1])
    for item in itertools.groupby(scientist, lambda x: x.field)
}

pprint(scientist_by_field)