n = [2, 3, 5, 6, 8, 9]

def oddIndexed(myList):
    '''Prints the odd indexed item'''
    newList=[]
    for i in range(len(myList)):
        if i%2 !=0:
            newList.append(myList[i])
    return tuple(newList)

print(oddIndexed(n))