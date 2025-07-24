"""Python Beginner Tutorial Testing"""

message = 'Hello world'
print(message[0])

alphabet=['A','B','C','D','E','F']
alphabet2=['A','B','C','D','E','F']
print(alphabet[0])

alphabet.append('G')
print(alphabet)

alphabet.insert(0,'H')
print(alphabet)


alphabet.extend(alphabet2)

alphabet.remove('G')

alphabet.pop()
'removes the last value like a stack'

alphabet.reverse()

alphabet.sort()
#sorts ascendantly
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

