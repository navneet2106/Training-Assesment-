class Multi (object):
    def __init__(self):
        self.str1 = "Navneet"
        print ("Multi")


class Multi2 (object):
    def __init__(self):
        self.str2 = "Bjhardwaj"
        print ("Multi2")


class Derived (Multi, Multi2):
    def __init__(self):

        Multi.__init__ (self)
        Multi2.__init__ (self)
        print ("Derived")

    def printStrs(self):
        print (self.str1, self.str2)


ob = Derived ()
ob.printStrs ()