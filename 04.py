"""
This script demonstrates the creation and basic manipulation of a 2D NumPy array.

Operations performed:
1. Creates a 2D NumPy array `y` with shape (2, 3).
2. Prints the shape of the array using `.shape`, which returns a tuple representing its dimensions.
3. Prints the number of dimensions (axes) using `.ndim`.
4. Performs element-wise multiplication of the array by 7.
5. Prints the resulting array after multiplication.
6. Displays the type of the object to confirm it's a NumPy ndarray.

This illustrates key properties and operations of NumPy arrays.
"""
import numpy as np

y = np.array([[1,2,3],[4,5,6]])

print("Shapes : ", y.shape)
print("-" * 50)
print("Dims : ", y.ndim)
print("-" * 50)
print(y * 7)
print("-" * 50)
print(type(y))