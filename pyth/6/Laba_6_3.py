with open('text/deti.txt', 'r', encoding='utf-8') as file:
    children_data = [line.strip().split() for line in file]

oldest_child = [None for x in range(3)]
youngest_child = [None for x in range(3)]
print(children_data)

for child in children_data:
    name = child[0] + child[1]
    age = int(child[2])

    if oldest_child[2] is None or (age > int(oldest_child[2])):
        oldest_child = child

    if youngest_child[2] is None or (age < int(youngest_child[2])):
        youngest_child = child

with open('text/oldest.txt', 'w') as file:
    file.write(' '.join(oldest_child) + '\n')

with open('text/youngest.txt', 'w') as file:
    file.write(' '.join(youngest_child) + '\n')