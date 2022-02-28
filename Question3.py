sample_text = "Learning Journal 2020"
letters=sum(c.isalpha() for c in sample_text)
numbers=sum(c.isnumeric() for c in sample_text)
print("Number of Letters:",letters)
print("Number of Digits:",numbers)