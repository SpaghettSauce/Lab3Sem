import random

a = []
for i in range(0, 5):
    a.append(random.randint(-100, 100))
print('Aray:', *a)


def sort(array):
    inc = len(array) // 2
    while inc:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc                                                            
            array[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

    return array

sort(a)
print('sorted array', *a)              #0-1582         #0