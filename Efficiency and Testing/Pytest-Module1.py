# The Pytest Module -part 1
# python beyond the basics - object oriented programming

"""
Unit Testing : The pytest module
Python tests are python programs that test other Python programs.
py.test looks for scripts functions/methods called test_.
After calling function or method, assert something is true.
with pytest.raises() to assert that an exception is raised.
setup_class() method to do test prep.
teardown_class() method to clean up after tests.
"""

import sys

def doubleit(x):
    var = x * 2
    return var

if __name__ == "__main__":
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)
    
    print(f"The value of {input_val} is {doubled_val}")
    
    
import myprogram

def test_doubleit():
    assert myprogram.doubleit(10) == 20
    
    




