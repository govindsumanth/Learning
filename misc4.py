import misc
import sys
print(sys.path)
#from misc3 import factorial
x=int(10)
print("Value is" , x)


x=5

def foo():
    global x
    x=x*2
    return x
print(foo())
print(misc.double(100))
#print(factorial(5))


import imp
import misc3
imp.reload(misc3)
print(dir(misc))