with open('text/input.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

numbers.sort()

with open('text/output2.txt', 'w') as file:
    for number in numbers:
        file.write(str(number))