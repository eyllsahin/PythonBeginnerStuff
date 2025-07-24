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

