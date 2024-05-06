from cytpes import *
from inspect import getmembers, isfunction

lib_hkl = cdll.LoadLibrary("/usr/local/lib/libhkl.so")
# or
lib_hkl = CDLL("/usr/local/lib/libhkl.so")
lib_hkl

print(getmembers(lib_hkl, isfunction))
# doesnt work, returns empty list

# trying to see what functions are in this shared library instance
