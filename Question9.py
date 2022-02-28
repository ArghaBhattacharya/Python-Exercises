sample_text = "Python is a high-level and general-purpose programming language"
my_list=sample_text.split(" ")
new_list=my_list[::-1]
new_text=" ".join(new_list)
print(new_text)