expr = input('Выражение: ')


open_close = 0      
for i in range(len(expr)):
    if expr[i] == '(':
        open_close += 1
    elif expr[i] == ')':
        open_close -= 1
if open_close != 0:
    print('Нарушены скобки')
    exit()


string_number = ''  
numbers, operations, priorities = [], [], [] 
max_priority = 0    
priority = 0       
for i in range(len(expr)):
    if expr[i] in '1234567890':
        string_number += expr[i]
    if expr[i] in '+-*/':
        if len(string_number) > 0:
            numbers.append(int(string_number))
            string_number = ''

        if expr[i] in '+-':
            priorities.append(priority)
            operations.append(expr[i])

        if expr[i] in '*/':
            priorities.append(priority + 1)
            operations.append(expr[i])
            if priority + 1 > max_priority:
                max_priority = priority + 1

    if expr[i] == '(':
        priority += 2
    if expr[i] == ')':
        priority -= 2
    if priority > max_priority:
        max_priority = priority

numbers.append(int(string_number))

while max_priority >= 0:
    i = 0
    while i < len(operations):
        if priorities[i] == max_priority:
            if operations[i] == '+':
                numbers[i] = numbers[i] + numbers[i + 1]
            elif operations[i] == '-':
                numbers[i] = numbers[i] - numbers[i + 1]
            elif operations[i] == '*':
                numbers[i] = numbers[i] * numbers[i + 1]
            elif operations[i] == '/':
                if numbers[i + 1] == 0:
                    max_priority = -10
                    break
                numbers[i] = numbers[i] / numbers[i + 1]
            numbers.pop(i + 1)
            operations.pop(i)
            priorities.pop(i)
            i -= 1
        i += 1
    max_priority -= 1

if max_priority > -10:
    print(numbers.pop())
else:
    print("Не делит на ноль")
