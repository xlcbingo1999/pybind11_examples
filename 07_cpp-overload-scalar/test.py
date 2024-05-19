import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())

import numpy as np
import example

print(example.mul(10.,20.))
print(example.mul(10 ,20.))
print(example.mul(10 ,20 ))

