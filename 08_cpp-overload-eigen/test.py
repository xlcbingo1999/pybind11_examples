import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())


import numpy as np
import example

A = np.array([[1,2,1],
              [2,1,0],
              [-1,1,2]])
B = 10

print(example.mul(A.astype(np.int  ),int  (B)))
print(example.mul(A.astype(np.float),float(B)))
