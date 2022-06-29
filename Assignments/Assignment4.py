import os

class ConfigkeyError(Exception):
    def __init__(self,this,key):
        self.key = key
        self.keys = this.keys()
        
    def __str__(self):
        return 'key "{0}" not found. Available keys: ({1})'.format(self.key,', '.join(self.keys))

class ConfigDict(dict):
    
    def __init__(self,filename):
        self._file = filename
        if not os.path.isfile(self._file):
            try:
                open(self._file,'r+').close()
            except IOError:
                raise IOError('arg to ConfigDict must be a valid pathname')
        with open(self._file) as file:
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
                
    def __getitem__(self, key):
        if not key in self:
            raise ConfigkeyError(self, key)
        return dict.__getitem__(self, key)
                
