# Benchmarking With TimeIt module
# Python beyond the basics - object oriented programming

"""
"Benchmarking" means comparing two code snippets to see which executed faster.
Time and memory are often not a concern to us, but it is to some python programmers.
Time tests should be run multiple times.
Tests should consider the context in which they will run.
Benchmarking is something of an art.
"""

import timeit

print('by index: ', timeit.timeit(stmt ="mydict['c']", setup="mydict = {'a':5,'b':6,'c':7}", number = 100000))
print('by get: ', timeit.timeit(stmt ="mydict.get('c')", setup="mydict = {'a':5,'b':6,'c':7}", number = 100000))