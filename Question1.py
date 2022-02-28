list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]
new_list1=list_1[1::2]
new_list2=list_2[::2]
new_list1.extend(new_list2)
print(new_list1)