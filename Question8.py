low=1
high=100
my_list=[]
for i in range(low,high+1):
    if i%3==0 and i%5==0:
        my_list.append(i)
print("Multiples of 3 and 5:",my_list)