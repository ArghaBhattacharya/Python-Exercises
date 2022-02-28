start = 20
end = 60
for num in range(start,end+1):
    for i in range(2,num//2):
        if num%i==0:
            break
    else:
        print(num)