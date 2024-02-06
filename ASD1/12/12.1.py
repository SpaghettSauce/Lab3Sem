import heapq
import os

BUFFER_SIZE = 50


def external_multiway_merge_sort(input_file, output_file):
    temporary_path = split_phase(input_file)
    merge_phase(temporary_path, output_file)
    for file in temporary_path:
        os.remove(file)


def split_phase(input_file):
    temporary_path = []
    with open(input_file, 'r') as file:
        temp_array = []
        count = 0
        for line in file:
            temp_array.append(int(line))
            count += 1
            if count >= BUFFER_SIZE:
                temp_array.sort()  
                temp_file = f"temp{len(temporary_path)}.txt"
                with open(temp_file, 'w') as temp:
                    temp.write('\n'.join(map(str, temp_array)))
                temporary_path.append(temp_file)
                temp_array = []
                count = 0
        if temp_array:
            temp_array.sort()  
            temp_file = f"temp{len(temporary_path)}.txt"
            with open(temp_file, 'w') as temp:
                temp.write('\n'.join(map(str, temp_array)))
            temporary_path.append(temp_file)
    return temporary_path


def merge_phase(temporary_path, output_file):
    min_heap = []
    for file in temporary_path:
        temp = open(file, 'r')
        first_number = int(temp.readline().strip())
        min_heap.append((first_number, temp))

    heapq.heapify(min_heap)

    with open(output_file, 'w') as output:
        while min_heap:
            minValue, temp = heapq.heappop(min_heap)
            output.write(str(minValue) + '\n')
            next_number = temp.readline().strip()
            if next_number:
                heapq.heappush(min_heap, (int(next_number), temp))
            else:
                temp.close()
    return

external_multiway_merge_sort('1.txt', 'output.txt')