# from youtube corey schafer

import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}{}@hooli.com'.format(self.first[0], self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)

#############################

# standard create instances using arguments
dev_1 = Developer('John', 'Doe', 10000, 'Python')

# creates new instances of class Employee with classmethod
emp_str1 = 'Jane-Sims-7000'
emp_str2 = 'Rick-Lee-5000'
emp_3 = Employee.from_string(emp_str1)
emp_4 = Employee.from_string(emp_str2)

# create Manager class and add an associated employee
mgr_1 = Manager('Morty', 'Link', 12000, [dev_1])
print('Listing employee under Manager attribute')
mgr_1.print_emps()

# use Manager methods to add/remove to the employees attribute
print('\nAdding employees to Manager attribute')
mgr_1.add_emp(emp_3)
mgr_1.add_emp(emp_4)
mgr_1.print_emps()

print('\nRemoving employee from Manager attribute')
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# special dunder methods
print('\nDemonstrate special dunder methods')
print('Dict', dev_1.__dict__)
print('Str', dev_1.__str__())

# dunder add method
print('\nDemonstrate dunder add method')
print(mgr_1 + dev_1)

# property decorator
print('\nDemonstrate Property decorator')
print(dev_1.first)
print(dev_1.last)
print(dev_1.email)
dev_1.last = 'Riley'

print(dev_1.fullname)
print(dev_1.email)

# setter
print('\nDemonstrate Setter')
dev_1.fullname = 'Jonathan Doe'
print('First name = ', dev_1.first)
print('Last name = ', dev_1.last)
print('Email = ', dev_1.email)

# deleter
print('\nDemonstrate Deleter')
del dev_1.fullname
print('First name = ', dev_1.first)
print('Last name = ', dev_1.last)

## Uses staticmethod
# my_date = datetime.date(2017, 7, 6)
# print(Employee.is_workday(my_date))

## More info on Developer class and inheritance
# print(help(Developer))

## Methods to check on classes and instances
# print(isinstance(mgr_1, Employee))
# print(issubclass(Developer, Manager))
