import numpy as np

def swap_str(arr):
    arr[[0, 2]] = arr[[2, 0]]
    return arr


array = np.arange(16).reshape(4, 4)
print("Array:")
print(array)


print("Arr with diff str:")
print(swap_str(array))