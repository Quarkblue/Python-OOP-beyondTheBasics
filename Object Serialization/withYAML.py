# Object Serialization with YAML
#python beyond the basics - object oriented programming

"""
YAML : Yaml Ain't Markup Language
Serializes python objects, like Pickle or json.
Uses whitespaces to separate elements.
    key: value
    key2: value2
    key3: 
    - listElement
    - listElement2
        - listelement3
        
Pyyaml install (*nix/MAC): sudo pip install pyyaml
Windows install depends on distro you are using.
"""

import yaml

mydict = {'a':1,'b':2,'c':3}
mylist = [1,2,3]
mytuple = (1,2,3)

loaded_yaml = yaml.dump(mydict, default_flow_style=False)
print(loaded_yaml)

print(yaml.dump(mylist, default_flow_style=False))
print(yaml.dump(mytuple, default_flow_style=False))