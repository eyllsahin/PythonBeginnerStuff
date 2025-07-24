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

