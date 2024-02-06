n = 3  

serpinski = ["*"]
for _ in range(n):
    triangle_size = len(serpinski)
    spaces = " " * triangle_size

    result = []
    for row in serpinski:
        result.append(spaces + row + spaces)
        spaces = spaces[:-1]  
    for row in serpinski:
        result.append(row + " " + row)

    serpinski = result

for row in serpinski:
    print(row)