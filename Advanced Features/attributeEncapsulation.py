# Attribute Encapsulation
# Python beyond the basics - object oriented programming

"""
Instance attributes can be changed anywhere, to any value,
breaking encapsulation.
Getter and Setter methods encourage encapsulation, but are
clunkier.
Users are expected to "do the right thing".
Trusting the user is pythonic.

@ property is a decorator that designates an instance attribute
as encapsulate-able through methods.
Getting,setting and deleting methods can be defined, called
automatically when a user accesses the attribute.
The names are linked to the attribute name - the methods, and
setter and deleter methods, must use it.
@property offers some control, but don't try to force the user
into certain behaviours - it's un-Pythonic.
"""


class GetSet(object):
    
    def __init__(self,value):
        self.attrval = value
        
    @property
    def var(self):
        print("Getting the var attribute")
        return self.attrval
    
    @var.setter
    def var(self,value):
        print("Setting the var attribute")
        self.attrval = value
        
    @var.deleter
    def var(self):
        print("Deleting the vat attribute")
        self.attrval = None


"""
@property should not encapsulate expensive operations, because
attribute setting looks cheap.
@property controls attributes that are epxected, but can't
control attributs that are unexpected.
__slots__ can define allowable attributes
    -Saves memory by defining attributes ahead of time.
    -Should not be used to limit attributes -un-Pythonic.
"""