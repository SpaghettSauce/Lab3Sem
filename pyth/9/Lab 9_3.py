import numpy as np

def massive_stats(arr):
    min_value = np.min(arr)
    max_value = np.max(arr)
    average_value = np.average(arr)
    standard_diviation = np.average(arr)
    return min_value, max_value, average_value, standard_diviation



array = np.random.randn(10, 4)
print("Array: ")
print(array)
print(" ")
print(massive_stats(array))
rows = array[:5]
print("5 rows: ")
print(rows)