import json

student = {
    'Name':'Samak',
    'Last_name':'Wardak',
    'Roll_no':'00912992',
    'Grade':'A',
    'Age':'22',
    'Subject':['Software Engineering', 'Graphic Designing', 'Data Structure']
}

with open('data.json', 'w') as write_file:
    json.dump(student, write_file)
    write_file.close()

b = json.dumps(student)
print(b)
