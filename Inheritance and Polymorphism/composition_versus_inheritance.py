# Composition versus Inheritance
# Python beyonds the basics - Object oriented programming

"""
Inheritance can be brittle(a change may require changes
elsewhere)
Decoupled code is classes, functions, etc. that work
independently and don't depend on one another.
As long as the interface is maintained, interactions between
classes will work.
Not checking or requiring particular types in polymorphic and
pythonic
"""

import random
import StringIO

class WriteMyStuff(object):
    
    def __init__(self,writer):
        self.writer = writer
        
    def write(self):
        write_text = "This is a message"
        self.writer.write(write_text)
        
        
fh = open('test.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()


sioh = StringIO.StringIO()
w2 = WriteMyStuff(sioh)

w2.write()
