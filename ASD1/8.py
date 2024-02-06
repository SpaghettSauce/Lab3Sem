import random

array = []
for i in range(0, 10):
    array.append(random.randint(-100, 100))
print('array:', *array)

positiv, negativ = [], []       
for i in range(len(array)):     
    if array[i] < 0:
        negativ.append(-array[i])
    else:
        positiv.append(array[i])
                                                                                
                                                                        # 01  12     22       #23   #24     #5
                         #24,23,5,01,12,22                                #0 #1     #2      #3     #4     #5
def countingSort(array, place):
    size = len(array)                                           #01,12,22,23,24,05
    output = [0] * size                                         
    count = [0] * 10    

    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    



    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]


# Основная функция 
def radixSort(array):
    max_element = max(array)
    place = 1
    while (max_element // place) > 0:
        countingSort(array, place)
        place *= 10

    return array

radixSort(negativ)
radixSort(positiv)

negativ.reverse()
for i in range(len(negativ)):
    negativ[i] = - negativ[i]

array = negativ + positiv

print('sorted array:', *(array))