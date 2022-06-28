# Private variable names
# Python beyond the basics - object oriented programming
"""
Variable Naming : "Public" and "Private"
"Public" attribute or variables(intended to be used by the 
importer of this module or user of this class):
regular_lower_case.

"Private" attributes or variables(internal use by the module
or class): _single_leading_underscore.

"Private" attribute that shouldn't be subclassed:
__double_leading_underscore.

"Magic" attributes: __double_underscores__
(use them, don't create them)
"""

from audioop import getsample


class GetSet(object):
    
    instance_count = 0
    
    __mangled_name = 'no privacy!'
    
    def __init__(self,value):
        self._attrval = value
        GetSet.instance_count += 1
        
    @property
    def var(self):
        print("Getting the 'var' attribute")
        return self._attrval
    
    @var.setter
    def var(self,value):
        print("setting the'var' attribute")
        self._attrval = value
        
    @var.deleter
    def var(self):
        print("deleting the 'var' attribute")
        self._attrval = None
        
        
        