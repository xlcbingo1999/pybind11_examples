import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())


import numpy as np
import example

A = np.arange(10).reshape(5,2)
B = example.length(A)

print('A = \n',A)
print('B = \n',B)
