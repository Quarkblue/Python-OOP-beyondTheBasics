# Implementing Core features
# Python beyonds the basics - Object oriented programming

class SumList(object):
    
    def __init__(self,this_list):
        self.myList = this_list
        
    def __add__(self,other):
        
        new_list = [ x + y for x,y in zip(self.myList, other.myList)]
        
        return SumList(new_list)
    
    def __repr__(self):
        return str(self.myList)
    
    
    
    
    
    