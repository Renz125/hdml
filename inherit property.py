#parent class
class Person(object):

    def __init__(self, name , idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class
class Employee( Person ):
    
    def __init__(self, name, idnumber,salary,post):
        self.salary = salary
        self.post = post

        # invoking  the _init_ of the parent class
        Person. __init__(self,name, idnumber)

#creation of an variable or an instance
a = Employee('Penguin', 5982491741, 919349, "intern")

#calling a function of the parent class using its instance
a.display()