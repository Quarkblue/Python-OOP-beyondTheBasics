# Debugging - PDB
# Python beyond the basics - object oriented programming

"""
Efficiency and Testing - PDB

Python Debugger.
built-in to Python.
Allows step-by-step execution of the script.
Allows flow control(can execute at any line or function).
Allows inspection of variables.
One of many debuggers; some IDEs show visual execution.
"""


import pdb

def doubleval(argsum,val):
    newval = argsum+val
    return newval

pdb.set_trace()

values = [1,2,3,4,5,6,7,8,9,10]

mysum = 0
for val in values:
    mysum = doubleval(mysum,val)
    
print(mysum)