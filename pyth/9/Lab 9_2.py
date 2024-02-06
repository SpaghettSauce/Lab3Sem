import numpy as np

def run_length_encoding(arr):
    return np.unique(arr, return_counts = True)
array = np.array([2,2,2,3,3,3,5])
run_len = run_length_encoding(array)
print(run_len)