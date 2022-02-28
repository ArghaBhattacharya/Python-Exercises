n = ['Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran']

def country(myList):
    '''Prints the name of countries starting with "A"'''
    newList=[]
    for i in range(len(myList)):
        c=myList[i]
        if c[0]=="A":
            newList.append(myList[i])
    return newList

print(country(n))