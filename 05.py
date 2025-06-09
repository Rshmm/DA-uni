"""
This script demonstrates how to create NumPy arrays initialized with specific values.

Operations performed:
1. Creates a 3x2 array `z` filled with zeros using `np.zeros()`.
2. Creates a 5x2 array `o` filled with ones using `np.ones()`.
3. Creates a 3x4 array `f` filled with the constant value 11 using `np.full()`.

Each array is then printed to show its contents and shape.

This highlights simple and common ways to initialize arrays with predefined values in NumPy.
"""

import numpy as np

z = np.zeros((3, 2))
print(z)

o = np.ones((5, 2))
print(o)

f = np.full((3, 4), 11)
print(f)
