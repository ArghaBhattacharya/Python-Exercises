def check(num):
    '''Checks whether number is present between 5 and 10 or not'''
    if num >= 5 and num <= 10:
        print("{} is present between 5-10.".format(num))
    else:
        print("{} is not present between 5-10.".format(num))

check(7)