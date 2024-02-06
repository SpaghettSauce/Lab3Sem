import numpy as np

def find_index(arr):
    index = np.nonzero(arr)[0]
    return index



array = np.array([0, 9, 1, 7, 2, 1, 2, 3, 4])
print(array)
 

 
print("Index:")
print(find_index(array))
