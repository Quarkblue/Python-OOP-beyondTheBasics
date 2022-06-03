class MaxSizelist:
      def __init__(self,maxSize):
            self.size = maxSize
            self.list = []
            
      def push(self,value):
            self.list.append(value)
            if len(self.list) > self.size:
                  self.list.pop(0)
                  
      def get_list(self):
            return self.list
      
      
      
a = MaxSizelist(3)

a.push("1")
a.push("2")
a.push("3")
a.push("4")

print(a.get_list())