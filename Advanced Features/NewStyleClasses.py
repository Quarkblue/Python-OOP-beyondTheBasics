# New style classes
# Python beyond the basics - object oriented programming
"""
New-Style Classes

Inherit from "object".
Can be constructed with default attributes from "metaclass"
constructors.
Allow the subclassing of built-ins
Allow the use of "slots" define instance attributes.
Use the "C3" MRO (method-resolution order).
Support "descriptors".
Are the only style of class in python 3.
"""

class OldClass():
    pass

class NewClass(object):
    pass

