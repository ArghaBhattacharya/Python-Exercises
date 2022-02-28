while True:
    try:
        num=int(input("Enter the number:"))
        print(num**2)
        break
    except Exception:
        print("Enter a valid input.")