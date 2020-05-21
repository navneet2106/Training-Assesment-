class Kloudone (object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print (self.name)
        print (self.idnumber)

    # child class


class Employee (Kloudone):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Kloudone.__init__ (self, name, idnumber)

    # creation of an object variable or an instance


a = Kloudone ('Navneet', 512000)

# calling a function of the class Person using its instance
a.display ()