# Example for inheriting the constructor
# Pythion beyond the basics - Object oriented programming

from __future__ import print_function
import random

class Animal(object):
    
    def __init__(self,name):
        self.name = name
        
        
class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.breed = random.choice(['Shih Tz', 'Beagle', 'Mutt'])
        
    def fetch(self,thing):
        print("%s goes after %s" % (self.name,thing))
        