from ctypes import *

from numpy import double

lib = cdll.LoadLibrary('/Users/cathyphi/Documents/APP2_SmartCalc_v3.0_Desktop_Python-1/src/libfoo.so')
lib.Model_parsing.restype = c_double

class PTEST(c_void_p): pass
lib.Model_parsing.argtypes = PTEST, c_wchar_p, c_double

class Model(object):
    def __init__(self):
        self.obj = lib.Model_new()

    def Parsing(self, x, value=1.0):
        return lib.Model_parsing(self.obj, x, value)

def presenter_calc(string: str, val_x):
    f = Model()
    x = f.Parsing(string, val_x)
    return x

if __name__ == "__main__":
    f = Model()
    s = "10000/2.369"
    x = f.Parsing(s)
    print(x)



