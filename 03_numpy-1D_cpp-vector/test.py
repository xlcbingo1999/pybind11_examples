import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())


import numpy as np
import example

A = [0,1,2,3,4,5]
B = example.multiply(A)

print('input list = ',A)
print('output     = ',B)

A = np.arange(10)
B = example.multiply(A)

print('input list = ',A)
print('output     = ',B)


