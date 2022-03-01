roll_numbers = {12, 7, 15, 23, 32, 30}
student_details = {12:'Judy', 30:'Shane', 23:'Aaron'}
set1=set(student_details.keys())
set2=roll_numbers.difference(set1)
print("Completed Applications:",set1)
print("Pending Applications:",set2)