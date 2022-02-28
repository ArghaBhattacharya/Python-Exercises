def stringReverse(string):
    """reverse a string if it's length is even"""
    if len(string) % 2 == 0:
        new_str = string[::-1]
        return new_str


try:
    print(stringReverse("Python"))
except TypeError:
    print("Check the string.")
except:
    print("Something went wrong.")