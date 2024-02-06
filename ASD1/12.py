import random

array = []
for i in range(0, 10):
    array.append(random.randint(-100, 100))
print('arr:', *array)


def merge_lists(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


def polyphase_merge_sort(input_list, block_size):

    temp_lists = []
    i = 0
    while i < len(input_list):
        block = input_list[i:i + block_size]
        block.sort()
        temp_lists.append(block)
        i += block_size
    
    while len(temp_lists) > 1:
        merged_lists = []
        i = 0
        while i < len(temp_lists):
            if i + 1 < len(temp_lists):
                
                merged = merge_lists(temp_lists[i], temp_lists[i + 1])
                merged_lists.append(merged)
                i += 2
            else:
                
                merged_lists.append(temp_lists[i])
                i += 1
        temp_lists = merged_lists

    sorted_list = temp_lists[0]
    return sorted_list


block_size = 1000  
print('Soeted arr:', *(polyphase_merge_sort(array, block_size)))