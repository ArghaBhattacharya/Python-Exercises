class InvalidNumError(Exception):
    pass


try:
    marks=int(input("Enter the marks:"))
    if marks<0 or marks>100:
        raise InvalidNumError("Error! Try again.")
    print("Results processing.")
except InvalidNumError as ine:
    print(ine)