num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}

print(set(num_1.keys()).intersection(set(num_2.keys())))
print(set(num_1.items()).intersection(set(num_2.items())))

s1=set(num_1.keys()).union(set(num_2.keys()))
s2=set(num_1.keys()).intersection(set(num_2.keys()))
print(s1.difference(s2))

num1_diff_num2_keys=set(num_1.keys()).difference(set(num_2.keys()))
print(num1_diff_num2_keys)

num_3=[]
num_4=[]
for key,value in num_1.items():
    for i in num1_diff_num2_keys:
        if i==key:
           num_3.append(key)
           num_4.append(value)
print(dict(zip(num_3,num_4)))