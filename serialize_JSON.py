import json

student = {
    'Name':'Samak',
    'Last_name':'Wardak',
    'Roll_no':'00912992',
    'Grade':'A',
    'Age':'22',
    'Gender': 'Male',
    'Subject':['Software Engineering', 'Graphic Designing', 'Data Structure']
}

# with open('Student_Data.json', 'w') as write_file:
#     json.dump(student, write_file)
#     write_file.close()

file = open('Student_Data.json', 'w')
json.dump(student, file)
file.close()

b = json.dumps(student)
print(b)
