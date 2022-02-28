letters_list = ['H', 'R', 'S']
new_list=[]
for i in range(1,4):
    for letters in letters_list:
        j=letters+str(i)
        new_list.append(j)
print(new_list)