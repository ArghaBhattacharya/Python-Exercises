list1=[1,2,3]
list2=[4,5,'abc']
try:
    new1=list1[2]+list2[3]
    new2=list1[2]+list2[2]
except IndexError:
    print("Invalid index, try again.")
except TypeError:
    print("Cannot add value of different types")