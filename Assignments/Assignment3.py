import os

class ConfigDict(dict):
    
    def __init__(self,filename):
        self._file = filename
        if os.path.isfile(self._file):
            with open(self._file,'r+') as file:
                lines = file.readlines()
                for line in lines:
                    line.rstrip()
                    key, value = line.split("=",1)
                    dict.__setitem__(self, key, value)
                    
    
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._file,'w') as file:
            for key,value in self.items():
                file.write('{0}={1}\n'.format(key,value))
                
