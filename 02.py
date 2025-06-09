"""
This script benchmarks the performance and memory usage of
native Python lists versus NumPy arrays when performing
element-wise multiplication on a sequence of 10 million integers.

It performs the following:
1. Creates a list of integers from 1 to 10,000,000.
2. Multiplies each element by 2 using a standard Python for-loop.
3. Measures and prints the time taken and memory consumed.

Then:
1. Creates a NumPy array of the same range.
2. Performs vectorized multiplication by 2.
3. Measures and prints the time taken and memory consumed.

This comparison highlights the efficiency of NumPy for large-scale
numerical operations in both speed and memory usage.
"""




import time
import sys
import numpy as np

start_time = time.time()


numbers = list(range(1,10000001, 1))

for i in range(len(numbers)):
    numbers[i] *= 2

end_time = time.time()

print(type(numbers))
print(f"These much time have been spend for these process{round(end_time-start_time, 2)}")
print(f"These much storage have been spend for these process{round(sys.getsizeof(numbers)/ 1024 ** 2, 2)} Megabytes")


start_time = time.time()

numbers = np.arange(1, 10000001, 1)
numbers = numbers * 2

end_time = time.time()

print("\nNUMPY")
print(type(numbers))
print(f"These much time have been spend for these process{round(end_time-start_time, 2)}")
print(f"These much storage have been spend for these process{round(sys.getsizeof(numbers)/ 1024 ** 2, 2)} Megabytes")