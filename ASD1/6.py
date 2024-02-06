import random

a = []
for i in range(0, 10):
    a.append(random.randint(-100, 100))
print('Array:', *a)


def sort(array):
    i = 0
    while i < len(array) - 1:
        m = i 
        j = i + 1

        while j < len(array):
            if array[j] < array[m]:
                m = j 
            j += 1

        array[i], array[m] = array[m], array[i]
    
        i += 1

    return array

sort(a)
print('Soretd array:', *a)            #70-431-25
                                      #|  |          #-4037