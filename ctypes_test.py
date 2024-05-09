from cytpes import *
from inspect import getmembers, isfunction

lib_hkl = cdll.LoadLibrary("/usr/local/lib/libhkl.so")
# or
lib_hkl = CDLL("/usr/local/lib/libhkl.so")
lib_hkl

res = lib_hkl.Detector.factory_new(lib_hkl.DetectorType(0))
print(res)



print(getmembers(lib_hkl, isfunction))
# doesnt work, returns empty list

# trying to see what functions are in this shared library instance
