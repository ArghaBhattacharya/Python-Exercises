def extraction(string):
    """extract first 10 letters of a string"""
    new_str = string[:10:]
    return new_str


try:
    new_string = input("Enter the string:")
    if len(new_string) < 10:
        raise ValueError("Oops! Too short string.")
    print(extraction(new_string))
except ValueError as ve:
    print(ve)