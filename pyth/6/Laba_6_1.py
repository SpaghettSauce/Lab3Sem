with open ("text/input.txt", "r") as file:
    numbers = [int(x) for x in file.read().split()]

multiply = 1
for number in numbers:
    multiply *= number

print(multiply)

with open ("text/output1.txt", "w") as file:
    file.write(str(multiply))