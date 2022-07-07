# Object Serialization with JSON
#python beyond the basics - object oriented programming

"""
JavaScript Object Notation
Extermely popular standard for storing and commuinicating data.
Human readable.
Often used for configuration files.
Resembles Python, but is not always valid Python.
"""

import json

with open('config.json') as file:
    conf = json.load(file)
    
conf['key'] = value

with open('config.json','w') as file:
    json.dump(conf,file)