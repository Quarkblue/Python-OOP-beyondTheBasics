import sys
from Assignments.Assignment3 import ConfigDict

cd = ConfigDict('config_file.txt')

key = "hell"
value = "h"
cd[key] = value
