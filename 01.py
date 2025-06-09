"""
This script demonstrates two different operations on a Python list:

1. List Replication:
   - Multiplies the list `numbers` by 2.
   - This does not perform element-wise multiplication.
   - Instead, it replicates the list, resulting in the list repeated twice.

2. Element-wise Multiplication:
   - Uses the `map()` function with a lambda to multiply each element of the list by 2.
   - Stores the result in `sqrs_numbers` and prints the new list.

This illustrates the difference between list replication and functional-style
element-wise operations in Python.
"""

numbers = [1,2,3,4,5]
print(numbers * 2 )  #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

sqrs_numbers = list(map(lambda x: x * 2, numbers)) # [2, 4, 6, 8, 10]
print(sqrs_numbers)