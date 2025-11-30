# The sys module.

#  The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within
#  Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.

import sys
from modules.hello import hello
sys.path.remove('/home/anton/python/beetroot_dz/dz/lesson9')
print(sys.path)