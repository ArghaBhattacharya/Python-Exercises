def student(subject_marks, name='None'):
    '''to print name and subjects where marks is more han 60'''
    list1 = []
    for subject, marks in subject_marks.items():
        if marks > 60:
            list1.append(subject)
    return "Name:{} - Subjects: {}".format(name, set(list1))


subject_marks = {'Mathematics': 80, 'Physics': 58, 'Chemistry': 62, 'English': 72, 'Biology': 50}
print(student(subject_marks, name='Brandon'))
