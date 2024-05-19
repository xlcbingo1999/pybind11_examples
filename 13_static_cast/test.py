import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{current_directory}/build/")

print("getpid: ", os.getpid())

import mymodule

print(mymodule.Foo().bar([1, 2, 3]))
print(mymodule.Foo().bar([1, 2, 3], 3))
