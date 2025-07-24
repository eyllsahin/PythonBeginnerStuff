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
