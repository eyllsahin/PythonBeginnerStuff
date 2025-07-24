'IMPORT MODULES'

import my_module  as mm
#/if you want to use one function use from my_module import find_index, test

courses=['Math','Physics','CompSci']

index=mm.find_index(courses,'Math')
print(index)

import datetime
import calendar

today=datetime.date.today()
print(today)

import os
print(os.getcwd())

print(os.__file__)#prints out the location of this file in the file system

#import antigravity #opens up a comic lol, uncomment for magic