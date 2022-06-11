# Decorators, Static and Class Methods
# Python beyond the basics - object oriented programming

# A decorator is a processor that modifies a function

#class method example
class InstanceCounter(object):
    count = 0
    
    def __init__(self,val):
        self.val = val
        InstanceCounter.count += 1
        
    def set_val(self,newVal):
        self.val = newVal
        
    def get_val(self):
        return self.val
    
    @classmethod
    def get_count(cls): 
        """
        "cls" in place of "self" because this method is a class
        method and doesn't need to be an instance method
        so also a decorated named "classmethod" is there
        """
        return cls.count
    

#static method example


class InstaceCounter(object):
    count = 0
    
    def __init__(self,val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1
        
    @staticmethod
    def filterint(value):
        """
        this method is neither an class method nor a instance
        method, but this is an utility method that does
        something useful and it belongs in the class code
        because it works with the class code but is neither an
        instance or a class method so we make it a static
        method.
        """
        if not isinstance(value, int):
            return 0
        else:
            return value

    