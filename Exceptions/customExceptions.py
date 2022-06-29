# Custom Exceptions
# Python beyond the basics - object oriented programming

class MyError(Exception):
    
    def __init__(self,*args):
        print("Calling init")
        if args:
            self.message = args[0]
        else:
            self.message = ''
            
    def __str__(self):
        print("Calling __str__")
        if self.message:
            return "here's a Myerror exception: " + self.message
        else:
            return "Here is a Myerror exception"