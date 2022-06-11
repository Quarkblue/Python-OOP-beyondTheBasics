# Method Overloading - Extending and Providing
# Python beyond the basics - object oriented programming

import abc

class GetSetParent(metaclass = abc.ABCMeta):
    
    def __init__(self,value):
        self.value = 0
        
    def set_val(self,value):
        self.val = value
        
    def get_val(self):
        return self.val
    
    @abc.abstractmethod
    def showdoc(self):
        return
    
    
class GetSetInt(GetSetParent):
    def set_val(self,value):
        if not isinstance(value, int):
            value = 0
        """
        if the value is not an integer then value is set as
        the superclass/parent classes method "set_val" result
        
        "super(GetSetInt,self)" means the parent class of "GetSetInt"
        """
        super(GetSetInt, self).set_val(value)
        
    def showdoc(self):
        print("GetSetInt object ({0}), only accepts integer values".format(id(self)))
        
class GetSetList(GetSetParent):
    
    def __init__(self,value=0):
        self.vallist = [value]
        
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    
    def set_val(self,value):
        self.vallist.append(value)
        
    def showdoc(self):
        print("GetSetList object, len{0}, stores history of values set".format(len(self.vallist)))