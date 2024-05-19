import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())

import example

A = [1.,2.,3.,4.]

B = example.modify(A)

print(B)

