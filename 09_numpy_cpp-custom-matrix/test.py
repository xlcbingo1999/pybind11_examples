import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())


import numpy as np
import example

A = np.arange(5)
B = np.arange(5)

print(example.mul(A,B))

A = np.arange(25).reshape(5,5)
B = np.arange(25).reshape(5,5)

print(example.mul(A,B))

A = np.arange(125).reshape(5,5,5)
B = np.arange(125).reshape(5,5,5)

print(example.mul(A,B))
