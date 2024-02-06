import numpy as np

def find_max_after_zero(arr):
    index = np.where(arr[:-1] == 0)[0]
    max_element = np.max(arr[index + 1])
    return max_element



array = np.array([1, 0, 8, 4, 3, 1, 2, 3, 8])
print("Array: ")
print(array)


print("Max element of arr: ")
print(find_max_after_zero(array))