class Person:
    def __init__(self, name):
        self.name= name

    def say_hi(self):
            print("Heloo, my name is ", self.name)
p = Person("Navneet BHardwaj")
p.say_hi()