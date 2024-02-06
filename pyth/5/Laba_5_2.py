def subset(set1, set2):
    return set1.issubset(set2)

set1 = {1, 2, 3}
set2 = {1, 4, 5}

set3 = {1, 2, 3, 4, 5, 6, 7}
set4 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}

set5 = {1, 10, 223, 413, 2}
set6 = {1, 10, 223, 413, 2}

print(subset(set1, set2))
print(subset(set3, set4))
print(subset(set5, set6))