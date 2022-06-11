# Inheritance example in python
# Python beyond the basics- object oriented programming

class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print('%s is eating %s' % (self.name,food))
        
class Dog(Animal):
    def fetch(self,thing):
        print('%s is fetching %s' % (self.name,thing))
        
class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string' % (self.name))
        
        