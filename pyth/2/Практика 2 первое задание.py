n = int(input())

triangle = []
row = [1]
for _ in range(n):
    triangle.append(row)
    next_row = [1]
    for i in range(len(row) - 1):
        next_row.append(row[i] + row[i + 1])
    next_row.append(1)
    row = next_row

for row in triangle:
    print(" ".join(map(str, row)).center(n * 3))