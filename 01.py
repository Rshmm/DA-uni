"""

We want to show the differences in python list and numpy array

"""

numbers = [1,2,3,4,5]
print(numbers * 2 )  #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

sqrs_numbers = list(map(lambda x: x * 2, numbers)) # [2, 4, 6, 8, 10]
print(sqrs_numbers)