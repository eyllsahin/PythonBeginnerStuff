"""Phython Beginner Tutorial Testing"""

message = 'Hello world'
print(message[0])

alphabet=['A','B','C','D','E','F']
alphabet2=['A','B','C','D','E','F']
print(alphabet[0])

alphabet.append('G')
print(alphabet)

alphabet.insert(0,'H')
print(alphabet)

alphabet.insert(0,alphabet2)

alphabet.extend(alphabet2)

alphabet.remove('G')

alphabet.pop()
'removes the last value like a stack'

alphabet.reverse()

alphabet.sort()
'sorts ascendantly'
print(alphabet)

sorted_alph= sorted(alphabet)
print(sorted_alph)

print(min(alphabet))
'or you can say max or sum too'

print(alphabet.index('A'))

print ('A' in alphabet)

for item in alphabet:
    'loops through the alphabet'
    print(item)

for index,alphabet in enumerate(alphabet):
    #gives the indexes also
  print(index,alphabet)


for index,alphabet in enumerate(alphabet, start=1):
    #gives the indexes also but starts from 1
  print(index,alphabet)

alphabet_str=', '.join(alphabet)
#we can write - instead of, as a delimiter
print(alphabet_str)

alphabet_str=' - '.join(alphabet) 
new_list= alphabet_str.split('-')
print(new_list)
print(alphabet_str)

'TUPLES'
tuple_1=('History','Math','Physics','CompSci') #will give en error
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)

tuple_1[0]='Art'
print(tuple_1) #tuples are immutable, it does not change

'SETS'
cs_courses = {'History','Math','Physics','CompSci'} #it gets rid of duplicates and does not care about order
print(cs_courses)
art_courses = {'History','Math','Physics','CompSci'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_set = set() #you cannot create an empty set with {} just like the others
empty_tuple=()
empty_tuple=tuple()
empty_list=[]
empty_list=list()


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

'CONDITIONALS'

'''Comparisons: 
Equal ==
Not Equal !=
Greater Than >
Less Than <
Greater or equal >=
Less or Equal <=
Object Identity is'''

language='Python'
if language=='Python':
    print('Its Python')
elif language=='Java':
    print('Its JAVA')
else:
    print('Its not Python or JAVA')


user='Admin'
logged_in=True

if user == 'Admin' and logged_in:  #you can say or instead of and
    print('You are logged in as Admin')
else:
    print('You are not logged in as Admin')


a= [1,2,3]
b= [1,2,3]
print(id(a))
print(id(b))
print(a==b)
print(a is b) #if we say a=b, then the prints will say True for both

'''The values that are False according to python
1-False
2-None
3-Zero, when say 10 will be True tho
4-Any empty sequence like '',(),[]
5-Any empty mapping like {} empty dictionary'''

'LOOPS AND ITERATIONS'

nums=[1,2,3]

for num in nums:
    if num==3:
        print('Found')
        break #if we say continue here, it will say found in 3 then continues instead of stopping
    print (num)

nums=[1,2,3]

for num in nums:
    for letter in 'Python':
        print(num,letter)

for i in range (1,11):
    print(i)

#or you can write it with while
x=0
while x < 10:
    print(x)
    x=x+1

 # If you want to add conditions
x = 0
while x < 10:
    if x==5:
        break
    print(x)
    x = x + 1  

'FUNCTIONS'


def hello_func():    #if you don't want to write a function just yet write pass
    pass


def hello_func():
    return 'Hello World!'
print(hello_func().upper())

def hello_func(greeting,name='You'):
   return '{} Function,{}'.format(greeting,name)

print(hello_func('Hello World'))
#if you want it to be local and want a default answer too


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math','Physics','CompSci',name="John")

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses=['Math','Physics','CompSci']
info={'name':'John','age':25}

student_info(*courses,**info)

'IMPORT MODULES'

import my_module  as mm
#/if you want to use one function use from my_module import find_index, test

courses=['Math','Physics','CompSci']

index=mm.find_index(courses,'Math')
print(index)



