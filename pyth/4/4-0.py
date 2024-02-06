
list = [1,9,5,6]

result = []
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        result.append(list[i])
print(result)