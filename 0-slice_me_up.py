#!/usr/bin/env python3
"""Slicing an array"""

arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]

arr1 = arr[:2]     # First two elements
arr2 = arr[-5:]    # Last five elements
arr3 = arr[1:6]    # Elements from index 1 to 5

print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))
