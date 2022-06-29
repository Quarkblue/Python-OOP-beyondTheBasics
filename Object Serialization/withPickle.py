# Object serialization with pickle
# python beyond the basics - object oriented programming

"""
Pickle and cPickle

Python-native object storage.
Can store most python objects on disk.
Does not store classes, modules or function, but can refer 
to them.
Not human readable.
Uses the pickle protocol which changes between versions of
python.
cPickle is a faster, C-compiled implementation
"""

import pickle

class MyClass(object):
    
    def __init__(self,init_val):
        self.val = init_val
    
    def increament(self):
        self.val += 1

cc = MyClass(5)
cc.increament()
cc.increament()

with open('datafile.txt','w') as file:
    pickle.dump(cc,file)
    
with open('datafile.txt','r') as file:
    loaded_data = pickle.load(file)
    
print(loaded_data)
print(loaded_data.val)