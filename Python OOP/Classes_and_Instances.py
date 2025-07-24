"""
This is the most basic way to create a class and instances
but,there is no use of the class at all so,
 the following way will make more sense
class Employee:
    pass
emp_1=Employee() #creating instances
emp_2=Employee()


emp_1.first='Corey'
emp_1.last='Smith'
emp_1.email='123@gmail.com'
emp_1.pay=50000

emp_2.first='Colly'
emp_2.last='Smog'
emp_2.email='45@gmail.com'
emp_2.pay=53000

print(emp_1.email)
print(emp_2.email)
"""


class Employee:
    def __init__(self, first, last, email, pay):  #constructor
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'  #or return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay * 1.15)

emp_1 = Employee('Corey', 'Smith', '123@gmail.com', 50000)
emp_2 = Employee('Colly', 'Smog', '45@gmail.com', 50000)

#print(emp_1.email)
#print(emp_2.email)
#print('The name is:{} {} Email: {} Pay: {}'.format(emp_1.first,emp_1.last, emp_1.email, emp_1.pay))
#since the code above is too long to type the info, we create a method that does that
#print(emp_1.fullname()) #usage of the method
