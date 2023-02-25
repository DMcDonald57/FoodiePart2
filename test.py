# import uuid

# token=(uuid.uuid4())
# print("Token: {}".format (token))


class ValueTooSmall(Exception):
    def __init__(self):
        super().__init__("The value is too small")

value = int(input("enter a number:"))
if(value <10):
    raise ValueTooSmall()

# exep1 = Exception("you hit an exception")
# exep2 = ValueTooSmall()
# print(exep1)
# print(exep2)

class Person:
    def __init__(self, f_name, l_name) -> None:
        self.first_name = f_name
        self.last_name = l_name
    def say_name(self):
        print(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, f_name, l_name, major):
        super().__init__(f_name, l_name)
        self.gpa = 2.5
        self.major = major

class Employee(Person):
    def __init__(self, f_name, l_name, pay=15):
        # if below arg not listed in def line, the value below is default
        # super code links person above to employee below.  Everyone is a person but not everyone
        # is an employeee
        super().__init__(f_name, l_name)
        self.pay = pay
        self.location = None
    def pay_raise(self,amount):
        self.pay = self.pay + amount

emp_one = Employee("John", "Doe")
emp_two = Employee("Jane", "Doe")
emp_three = Employee("Jack", "Doe", "20")


emp_one.say_name()
emp_two.say_name()
print (emp_one.pay)
emp_one.pay_raise(2)
print(emp_one.pay)
print(emp_three.pay)


# print(emp_one.first_name, emp_one.last_name)
# print(emp_two.first_name, emp_two.last_name)
# print(emp_one.__dict__)
