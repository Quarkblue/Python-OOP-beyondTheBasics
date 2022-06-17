# SubClassing Built-In's
# Python beyond the basics - object oriented programming

"""
Here we are inheriting from a built in class "dict"
from which we can access all the properties of the dictionries
in python and implement our own.
as you can see in the given example below.
"""

class MyDict(dict):
    
    def __setitem__(self, key, value):
        print("Setting a key and value")
        dict.__setitem__(self, key, value)