import random

a = []
for i in range(0, 10):
    a.append(random.randint(-100, 100))
print('Array:', *a)


def combsort(array):
    gap = len(array)
    flag = True
    while gap != 1 or flag:
        if gap > 1:
            gap = int(gap * 10 / 13)
        flag = False
        i = 0
        for i in range (gap,len(array)):
            if (array[i - gap] > array[i]):
                tmp = int(array[i])
                array[i] = array[i - gap]
                array[i - gap] = tmp
                flag = False
            
        
    return array

a = combsort(a)
print('CombSorted array:', *a)