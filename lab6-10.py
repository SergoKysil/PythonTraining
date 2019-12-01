# class Vehicle:
#
#     def __init__(self, brand, model, color, price):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.price = price
#         self.car_name = brand + ' ' + model
#
#
# car_1 = Vehicle('Mazda', 'RX-8', 'Black', 80000)
# car_2 = Vehicle('Nisan', 'GT-R', 'White', 10000)
#
# print (car_1.car_name)
#
# print (car_2.car_name)
# print (car_1)
# print (car_2)


class Employee:
    num_of_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emp += 1

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
        print('Name Deleted!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def _repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.first + ' ' + other.last

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees = None ):
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
            print('-->', emp.fullname())


dev_2 = Developer('Sergo', 'Kysil', 10000, 'C++')
dev_1 = Developer('Muhaylo', 'Programer', 10000, 'QT')

emp_str1 = 'Vitya-Java-10000'
new_emp_1 = Employee.from_string(emp_str1)

mgr_1 = Manager('Syava', 'Bogart', 90000, [dev_1])

print(dev_2.email)

