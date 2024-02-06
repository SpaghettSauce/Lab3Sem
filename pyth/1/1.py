# 1 задание

def check(a,b,c):
    if a == b and b == c:
        return 3
    if a == b or a == c or b == c:
        return 2
    if a != b and a != c and b != c:
        return 0
print(check(int(input("Input: ")),int(input()),int(input())))

# 2 задание (решение со строками)

n = int(input("Num of steps: "))
str1 = ''
for i in range(1, n+1):
    str1 += str(i)
    print(str1)

# 2 задание (решение без строк)

n = int(input("Num of steps: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j,end='')
    print()

# задание 3

n = int(input("Number of rows: ")) + 1
for i in range(1, n + 1):
    print(' ' * (n - i), end='') # количество пробелов от чисел и до границ консоли
    print(*range(1, i), *range(1, i - 1)[::-1], sep='') # числа слева и справа относительно центра пирамиды

# 4 задание

num = int(input("Num of rows: "))
def smoothStr(i): # функция для выравнивания строк по пробелам
    s = ""
    if i < 10: # выравниваем всё до 10 элемента
        s = "  "
    elif i < 100: # выравниваем всё до 100 элемента
        s = " "
    return s + str(i)

allrows = ""
for j in range(1, num + 2):
    # количество пробелов от чисел и до границ консоли
    row = " " * 4 * (num - j + 1)
    # левая часть
    for i in range(1, j):
        s = smoothStr(i)
        row += s + " "
    # правая часть
    for i in range(j-1, 1,-1):
        s = smoothStr(i-1)
        row += s + " "
    row += "\n"
    allrows += row

print(allrows)
