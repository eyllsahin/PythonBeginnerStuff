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

import datetime
class Employee:
    num_of_employees = 0              # Class variable to count all employees
    raise_amount = 1.04               # Default raise amount

    def __init__(self, first, last, pay):  # Constructor
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):       # Changes class-wide raise amount
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):        # Alternate constructor using string
        first, last, pay = emp_string.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):                     # Utility method unrelated to class/instance
        return day.weekday() not in (5, 6)

class Developer(Employee):
    raise_amount = 1.1                       # Override raise for developers

    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)   # Call Employee constructor
        self.lang = lang                     # Add new property: programming language

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees if employees else []

    def add_emp(self, emp):                  # Add employee to team
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):               # Remove employee from team
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):                    # Display team members
        for emp in self.employees:
            print('---->', emp.fullname())

dev_1 = Developer('Corey', 'Smith', 50000, 'python')
dev_2 = Employee('Colly', 'Smog', 50000)

mngr_1 = Manager('John', 'Smith', 50000, [dev_1])
print(mngr_1.email)

mngr_1.print_emps()         # Shows dev_1
mngr_1.add_emp(dev_2)       # Add dev_2 to manager
mngr_1.remove_emp(dev_1)    # Remove dev_1
mngr_1.print_emps()         # Should show only dev_2 now

print(isinstance(mngr_1, Manager))   # True
print(isinstance(Manager, Developer))# False (not object instance)
print(isinstance(mngr_1, Employee))  # True, Manager is subclass of Employee

print(dev_1.email)                   # corey.smith@gmail.com
print(dev_2.email)                   # colly.smog@gmail.com

print(dev_1.pay)                     # 50000
dev_1.apply_raise()
print(dev_1.pay)                     # 55000 after 10% raise
print(dev_1.lang)                    # 'python'

print(Employee.is_workday(datetime.date(2021, 1, 1)))  # Friday → True

Employee.set_raise_amount(1.2)      # Affects all future Employee instances
print(dev_2.raise_amount)           # Will show 1.2 unless overridden individually

emp_str_1 = 'ayse-Nihal-30000'
emp_str_2 = 'afkn-Nihal-30060'
emp_str_3 = 'HDJHK-Nihal-35000'

emp1_obj = Employee.from_string(emp_str_1)
print(emp1_obj.__str__())           # Default __str__ unless overridden

dev_2.raise_amount = 1.09

print(dev_2.__dict__)               # See all attributes of dev_2
print(dev_2.pay)                    # Show current pay
print(Employee.raise_amount)        # Show current class-wide raise
print(dev_2.raise_amount)           # Show instance override

print(Employee.num_of_employees)    # Total number of employees created
print('The name is:{} {} Email: {} Pay: {}'.format(dev_2.first, dev_2.last, dev_2.email, dev_2.pay))
print(dev_2.fullname())             # Cleaner method call
