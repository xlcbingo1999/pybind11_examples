import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())

import numpy as np
import example

A = np.arange(10)

print('A = \n',A)

array = example.CustomVectorXd(A)

print('array.mul(default) = \n'   ,array.mul()          )
print('array.mul(factor=100) = \n',array.mul(factor=100))

print('trans(A) = \n',example.trans(A))
