list_1 = [1, 5, 8]
list_2 = [3, 2, 5]
list_3 = [2, 3, 6]

sum_of_list = list(map(lambda x, y, z: x + y + z, list_1, list_2, list_3))

print(sum_of_list)