"""
This script demonstrates the conversion of a native Python list to a NumPy array.

Steps performed:
1. Creates a standard Python list `x` containing integers.
2. Prints the type and content of the list.
3. Converts the list to a NumPy array `y` using `np.array()`.
4. Prints the type and content of the resulting NumPy array.

This illustrates the basic difference in data types between Python lists and NumPy arrays.

"""

import numpy as np

x = [1,2,3,4,5]
print(type(x))
print(x)

print("-" * 50)

y = np.array(x)
print(type(y))
print(y)