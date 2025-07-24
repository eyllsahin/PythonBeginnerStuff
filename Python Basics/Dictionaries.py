"ctrl f5 run"
'DICTIONERIES'
student={'name' : 'John','age':25, 'courses': ['Math','Physics','CompSci']} #instead of name, you can say whatever 1 for instance
print(student['name'])
student['name'] = 'Ali'
print(student['name'])

student.update({'name':'Halil','age':25})
print(student)

age=student.pop('age')
print(age)

print(student.items())

print(student.get('range','Not found'))

for key,value in student.items(): #looping through
 print(key,value)


