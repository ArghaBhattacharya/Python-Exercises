map_details = {101: 'Park', 102: 'Zoo', 103: 'Mall'}


def find(my_list):
    '''to find the key of value "Mall"'''
    for key, value in my_list.items():
        if value == 'Mall':
            return key


print(find(map_details))