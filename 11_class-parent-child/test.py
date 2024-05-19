import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())

import example

print(example.talk(example.Dog(),2))
print(example.talk(example.Cat(),3))
