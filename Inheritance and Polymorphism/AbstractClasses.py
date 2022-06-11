# Abstract classes
# Python beyonds the basics - Object oriented programming
"""
An Abstract class is a kind of model for other classes to
be defined. It is not designed to construct instances, but
can be subclasses by regular classes

Abstract classes can define an interface, or merthods that
must be implemented by its subclasses.
"""


import abc
"""
the python abc module enables the creation of abstract
base classes
"""

class GetterSetter(metaclass=abc.ABCMeta): # have to define metaclass in the class argument
    
    @abc.abstractmethod # place decorators for defining abstract methods
    def set_val(self,input):
        return
    
    @abc.abstractmethod
    def get_val(self):
        return
    
    
    
class MyClass(GetterSetter):
    
    def set_val(self,input):
        self.val = input
        
    def get_val(self):
        return self.val
    
        
        
x = MyClass()
print(x)
