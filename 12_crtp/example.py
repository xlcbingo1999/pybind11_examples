import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())


import mymodule
import numpy as np

A = np.array([1, 2, 3])

assert np.all(mymodule.Base().myfunc(A) == 2 * A)
assert np.all(mymodule.Derived().myfunc(A) == 3 * A)
