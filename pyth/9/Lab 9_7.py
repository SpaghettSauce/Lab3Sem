import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

values_column = iris[:, -1]
unique_values, counts = np.unique(values_column, return_counts=True)
print("Unique val:")
print(unique_values)

print("Amount:")
print(counts)