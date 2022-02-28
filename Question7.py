num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
minimum = min(num_list,key=sum)
maximum = max(num_list,key=sum)
print("The list with the maximum sum of elements: {}".format(maximum))
print("The list with the minimum sum of elements: {}".format(minimum))