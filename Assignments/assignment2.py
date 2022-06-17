import abc
from datetime import datetime

class WriteFile(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def write(self):
        return
    
    def __init__(self,filename):
        self.filename = filename
        
    def write_line(self,text):
        fh = open(self.filename, 'a')
        fh.write(text + "\n")
        fh.close()
        
        
class DelimFile(WriteFile):
    
    def __init__(self,filename,delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim
        
    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)
        
class Logfile(WriteFile):
    
    def write(self,this_line):
        dt = datetime.now()
        date_str = dt.strtime('%Y-%m-%d %H:%M')
        self.write_line('{0}    {1}'.format(date_str,this_line))