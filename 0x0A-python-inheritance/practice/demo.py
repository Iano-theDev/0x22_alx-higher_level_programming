#!/usr/bin/python3
class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage
        
    def view(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self, fname, fage):
        parent.__init__(self, fname, fage)
        self.lastname
        
                
ob = Child()
ob.func1()
ob.func2()