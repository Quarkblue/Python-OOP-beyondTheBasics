# Polymorphism example in python
# python beyond the basics- object oriented programming


class Animal(object):
    
    def __init__(self,name):
        self.name = name
        
    def eat(self,food):
        print("{0} eats {1}".format(self.name,food))
        
        
class Dog(Animal):
    
    def fetch(self,thing):
        print("{0} goes after the {1}".format(self.name,thing))
        
    def show_affections(self):
        print("{0} wags tail".format(self.name))
        
class Cat(Animal):
    
    def swatstring(self):
        print("{0} shreds the string".format(self.name))
        
    def show_affections(self):
        print('{0} purrs'.format(self.name))
        