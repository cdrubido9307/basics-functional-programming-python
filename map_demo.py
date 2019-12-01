from inmutable_data_structure import scientist

name_and_ages = tuple(map(lambda x: {'name': x.name, 'age': 2019 - x.born}, scientist))

for i in name_and_ages:
    print(i)