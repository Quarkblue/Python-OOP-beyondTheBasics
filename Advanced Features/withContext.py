# With context
# Python beyond the basics - object oriented programming
"""
__with__ context
Some objects need to "clean up" when done
    File object needs to close().
    A network connection may need to close.
    A data-intensive operations may need to del data.
__with__ provides a block that cleans up when exited.
Can handle exception that occur withing the block.
Can also execute code when entered.
"""


class Myclass(object):
    
    def __enter__(self):
        print("We have entered 'with'")
        return self
    
    def __exit__(self, type,value,traceback):
        print("We are leaving 'with'")
        
    def sayhi(self):
        print("Hi, instance %s" % (id(self)))
        
        
